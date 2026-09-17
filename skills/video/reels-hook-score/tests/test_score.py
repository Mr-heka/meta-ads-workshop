#!/usr/bin/env python3
# Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠
# Provenance marker: sk-0dnoqd
import csv
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "score.py"
SPEC = importlib.util.spec_from_file_location("reels_hook_score", SCRIPT)
SCORE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SCORE)


def run_score(input_path, outdir, *extra):
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(input_path), "--start", "2026-08-01", "--end", "2026-08-31", "--rank-metrics", "hold_3s_rate,completion_rate", "--composite", "--top", "1", "--outdir", str(outdir), *extra],
        text=True,
        capture_output=True,
        check=False,
    )


class ScoreTests(unittest.TestCase):
    def write_csv(self, directory, text):
        path = directory / "input.csv"
        path.write_text(text, encoding="utf-8")
        return path

    def test_source_filename_and_exact_date_contract(self):
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            source = temp / "source`x.csv"
            source.write_text("id,posted,hold_3s_rate,completion_rate\na,2026-08-01,0.4,0.5\nb,2026-08-02,0.5,0.6\n")
            outdir = temp / "report"
            result = run_score(source, outdir)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Source: source\\`x.csv (", (outdir / "dashboard.md").read_text())
            for value in ("20260801", "2026-W31-6"):
                source.write_text("id,posted,hold_3s_rate,completion_rate\na," + value + ",0.4,0.5\nb,2026-08-02,0.5,0.6\n")
                rejected = run_score(source, temp / value)
                self.assertEqual(rejected.returncode, 2)
                self.assertFalse((temp / value).exists())

    def test_underflow_is_not_a_measured_zero(self):
        base = [{"id": "a", "posted": "2026-08-01", "hold_3s_rate": 0.4, "completion_rate": 0.5},
                {"id": "b", "posted": "2026-08-02", "hold_3s_rate": 0.5, "completion_rate": 0.6}]
        cases = [("json", json.dumps([dict(base[0], watch_ratio="TOKEN"), base[1]]).replace('"TOKEN"', '1e-999')),
                 ("json", json.dumps([dict(base[0], saves=1, views=10 ** 400), base[1]])),
                 ("csv", "id,posted,hold_3s_rate,completion_rate,watch_ratio\na,2026-08-01,0.4,0.5,1e-999\nb,2026-08-02,0.5,0.6,1\n")]
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            for index, (suffix, content) in enumerate(cases):
                with self.subTest(index=index):
                    source = temp / ("input." + suffix)
                    source.write_text(content)
                    outdir = temp / str(index)
                    result = run_score(source, outdir)
                    self.assertEqual(result.returncode, 2, result.stderr)
                    self.assertIn("underflows", result.stderr)
                    self.assertFalse(outdir.exists())

    def test_numeric_overflow_fails_before_reservation(self):
        base = [{"id": "a", "posted": "2026-08-01", "hold_3s_rate": 0.4, "completion_rate": 0.5},
                {"id": "b", "posted": "2026-08-02", "hold_3s_rate": 0.5, "completion_rate": 0.6}]
        cases = [json.dumps({"data": base, "unknown": "TOKEN"}).replace('"TOKEN"', '1e999')]
        for fields in ({"average_watch_seconds": 1e308, "duration_seconds": 1e-308},
                       {"views": 1, "saves": 10 ** 400},
                       {"hold_3s_rate": 10 ** 400}):
            cases.append(json.dumps([dict(base[0], **fields), base[1]]))
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            for index, content in enumerate(cases):
                with self.subTest(index=index):
                    source = temp / "input.json"
                    source.write_text(content)
                    outdir = temp / str(index)
                    result = run_score(source, outdir)
                    self.assertEqual(result.returncode, 2, result.stderr)
                    self.assertIn("finite", result.stderr)
                    self.assertNotIn("Traceback", result.stderr)
                    self.assertFalse(outdir.exists())

    def test_cohort_report_retains_raw_evidence_and_marks_missing(self):
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            source = self.write_csv(temp, """id,posted,caption,views,saves,shares,hold_3s_rate,completion_rate,verified_audiovisual_opener,audiovisual_opener_verified
a,2026-08-03,Stop using vague hooks,1000,50,20,0.72,0.60,Speaker says stop,true
b,2026-08-10," \t=formula opener",900,18,10,0.79,0.88,,
c,2026-07-30,Outside cohort,700,10,5,0.80,0.80,,
d,2026-08-16,Missing completion remains visible,500,4,1,0.40,,,
e,,No posting date remains visible,400,4,1,0.40,0.50,,
""")
            outdir = temp / "report"
            result = run_score(source, outdir)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual({path.name for path in outdir.iterdir()}, {"input.raw", "normalized.json", "provenance.json", "dashboard.md", "top10.csv", "bottom10.csv", "hook_patterns.md"})
            rows = json.loads((outdir / "normalized.json").read_text())["rows"]
            by_id = {row["id"]: row for row in rows}
            self.assertEqual(by_id["c"]["cohort_status"], "outside_cohort")
            self.assertEqual(by_id["e"]["cohort_status"], "missing_posted_not_ranked")
            self.assertEqual(by_id["d"]["metrics"]["completion_rate"], None)
            self.assertIsNone(by_id["d"]["cohort_score"])
            self.assertEqual(by_id["b"]["caption_opener_raw"], " \t=formula opener")
            self.assertIsNone(by_id["b"]["verified_audiovisual_opener"])
            self.assertIn(b"\t=formula opener", (outdir / "input.raw").read_bytes())
            with (outdir / "top10.csv").open(newline="", encoding="utf-8") as handle:
                output_rows = list(csv.DictReader(handle))
            self.assertTrue(output_rows)
            self.assertEqual(output_rows[0]["caption_opener"], "' \t=formula opener")
            dashboard = (outdir / "dashboard.md").read_text(encoding="utf-8")
            self.assertIn("heuristic", dashboard)
            self.assertIn("outside_cohort", dashboard)

    def test_invalid_unit_duplicate_and_nonfinite_leave_no_output(self):
        cases = [
            ("invalid-rate", "id,posted,hold_3s_rate,completion_rate\na,2026-08-01,45%,0.5\nb,2026-08-02,0.4,0.5\n", "plain normalized decimal"),
            ("duplicate", "id,posted,hold_3s_rate,completion_rate\na,2026-08-01,0.4,0.5\na,2026-08-02,0.5,0.6\n", "duplicate id"),
            ("nonfinite", "id,posted,hold_3s_rate,completion_rate\na,2026-08-01,NaN,0.5\nb,2026-08-02,0.5,0.6\n", "plain normalized decimal"),
        ]
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            for name, content, expected in cases:
                source = self.write_csv(temp, content)
                outdir = temp / name
                result = run_score(source, outdir)
                self.assertEqual(result.returncode, 2)
                self.assertIn(expected, result.stderr)
                self.assertFalse(outdir.exists())

    def test_unverified_audiovisual_claim_and_implicit_composite_fail(self):
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            source = self.write_csv(temp, """id,posted,hold_3s_rate,completion_rate,verified_audiovisual_opener
a,2026-08-01,0.4,0.5,Opening spoken line
b,2026-08-02,0.5,0.6,Other opening
""")
            outdir = temp / "unverified"
            result = run_score(source, outdir)
            self.assertEqual(result.returncode, 2)
            self.assertIn("requires audiovisual_opener_verified true", result.stderr)
            self.assertFalse(outdir.exists())
            valid = self.write_csv(temp, """id,posted,hold_3s_rate,completion_rate
a,2026-08-01,0.4,0.5
b,2026-08-02,0.5,0.6
""")
            implicit = subprocess.run([sys.executable, str(SCRIPT), str(valid), "--start", "2026-08-01", "--end", "2026-08-31", "--rank-metrics", "hold_3s_rate,completion_rate", "--outdir", str(temp / "implicit")], text=True, capture_output=True, check=False)
            self.assertEqual(implicit.returncode, 2)
            self.assertIn("require --composite", implicit.stderr)

    def test_json_rows_use_per_row_aliases_and_preserve_measured_zero(self):
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            source = temp / "input.json"
            source.write_text(json.dumps({"data": [
                {"id": "zero-a", "posted": "2026-08-03", "hold_3s_rate": 0, "completion_rate": 0},
                {"reel_id": "zero-b", "posted_date": "2026-08-04", "hold_3s_rate": 0, "completion_rate": 0},
            ]}), encoding="utf-8")
            outdir = temp / "json-report"
            result = run_score(source, outdir)
            self.assertEqual(result.returncode, 0, result.stderr)
            rows = json.loads((outdir / "normalized.json").read_text())["rows"]
            self.assertEqual({row["id"] for row in rows}, {"zero-a", "zero-b"})
            self.assertTrue(all(row["metrics"]["hold_3s_rate"] == 0 for row in rows))
            self.assertTrue(all(row["metrics"]["completion_rate"] == 0 for row in rows))
            self.assertTrue(all(row["rank"] is not None for row in rows))
            self.assertEqual({row["rank"] for row in rows}, {1})

    def test_strict_structural_parsing_and_concurrent_destination(self):
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            cases = [
                (temp / "duplicate.json", '{"data":[{"id":"a","id":"other","posted":"2026-08-01","hold_3s_rate":0.4,"completion_rate":0.5}]}', "JSON has duplicate key"),
                (temp / "extra.csv", "id,posted,hold_3s_rate,completion_rate\na,2026-08-01,0.4,0.5,extra\n", "has 5 cells; expected 4"),
                (temp / "missing.csv", "id,posted,hold_3s_rate,completion_rate\na,2026-08-01,0.4\n", "has 3 cells; expected 4"),
            ]
            for source, content, expected in cases:
                source.write_text(content, encoding="utf-8")
                result = run_score(source, temp / (source.stem + "-out"))
                self.assertEqual(result.returncode, 2)
                self.assertIn(expected, result.stderr)
            source = self.write_csv(temp, """id,posted,hold_3s_rate,completion_rate
a,2026-08-01,0.4,0.5
b,2026-08-02,0.5,0.6
""")
            reserved = temp / "concurrent-writer"
            reserved.mkdir()
            (reserved / "creator.txt").write_text("other writer", encoding="utf-8")
            result = run_score(source, reserved)
            self.assertEqual(result.returncode, 2)
            self.assertIn("created concurrently", result.stderr)
            self.assertEqual((reserved / "creator.txt").read_text(encoding="utf-8"), "other writer")

    def test_unbounded_event_ratios_watch_ratio_and_bounded_dashboard(self):
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            long_caption = "  " + "x" * 250000
            source = self.write_csv(temp, """id,posted,caption,views,saves,average_watch_seconds,duration_seconds,replays,unique_viewers,watches_per_viewer,extra_export_field
a,2026-08-01,"{}",2,5,12,10,20,10,5,kept-as-ignored
b,2026-08-02,normal,2,2,8,10,2,2,3,kept-as-ignored
""".format(long_caption))
            outdir = temp / "ratio-report"
            result = subprocess.run([sys.executable, str(SCRIPT), str(source), "--start", "2026-08-01", "--end", "2026-08-31", "--rank-metrics", "saves_per_view,watch_ratio,replays_per_viewer", "--composite", "--outdir", str(outdir)], text=True, capture_output=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            rows = {row["id"]: row for row in json.loads((outdir / "normalized.json").read_text())["rows"]}
            self.assertEqual(rows["a"]["metrics"]["saves_per_view"], 2.5)
            self.assertEqual(rows["a"]["metrics"]["watch_ratio"], 1.2)
            self.assertEqual(rows["a"]["metrics"]["replays_per_viewer"], 2.0)
            self.assertEqual(rows["a"]["metrics"]["watches_per_viewer"], 5.0)
            self.assertEqual(len((outdir / "dashboard.md").read_bytes()) < 200 * 1024, True)
            self.assertIn("extra_export_field", json.loads((outdir / "provenance.json").read_text())["input"]["ignored_source_fields"])
            self.assertIn(long_caption.encode("utf-8"), (outdir / "input.raw").read_bytes())
            bad = self.write_csv(temp, """id,posted,views,saves,hold_3s_rate,completion_rate
a,2026-08-01,0,1,0.4,0.5
b,2026-08-02,1,0,0.5,0.6
""")
            rejected = run_score(bad, temp / "zero-count")
            self.assertEqual(rejected.returncode, 2)
            self.assertIn("zero views cannot have positive saves", rejected.stderr)

    def test_owned_publication_keeps_failure_receipt(self):
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            outdir = temp / "reserved"
            ownership = SCORE.reserve_output_directory(outdir)
            concurrent_target = temp / "concurrent-dashboard"
            concurrent_target.write_text("concurrent writer", encoding="utf-8")
            (outdir / "dashboard.md").symlink_to(concurrent_target)
            (outdir / "FAILED.json").write_text("existing receipt", encoding="utf-8")
            with self.assertRaises(SCORE.ValidationError):
                SCORE.publish_reserved(outdir, ownership, {"dashboard.md": "replacement"})
            self.assertTrue((outdir / "dashboard.md").is_symlink())
            self.assertEqual(concurrent_target.read_text(encoding="utf-8"), "concurrent writer")
            self.assertEqual((outdir / "FAILED.json").read_text(encoding="utf-8"), "existing receipt")

    def test_exact_json_counts_wrapper_provenance_and_constants_fail_before_reservation(self):
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            source = temp / "wrapped.json"
            source.write_text("""{"account_name":"example-account","export_version":3,"data":[
{"id":"a","posted":"2026-08-01","views":9007199254740993,"hold_3s_rate":0.8,"completion_rate":0.7},
{"id":"b","posted":"2026-08-02","views":2,"hold_3s_rate":0.4,"completion_rate":0.5}
]}""", encoding="utf-8")
            outdir = temp / "wrapped-report"
            result = run_score(source, outdir)
            self.assertEqual(result.returncode, 0, result.stderr)
            rows = {row["id"]: row for row in json.loads((outdir / "normalized.json").read_text())["rows"]}
            self.assertEqual(rows["a"]["views"], 9007199254740993)
            self.assertIsInstance(rows["a"]["views"], int)
            provenance = json.loads((outdir / "provenance.json").read_text())
            self.assertEqual(provenance["input"]["container"], {"kind": "object_container", "container_key": "data", "metadata": {"account_name": "example-account", "export_version": 3}})
            self.assertTrue({"account_name", "export_version"}.issubset(provenance["input"]["ignored_source_fields"]))
            bad = temp / "constant.json"
            bad.write_text('{"data":[{"id":"a","posted":"2026-08-01","hold_3s_rate":0.4,"completion_rate":0.5,"unknown_metric":NaN},{"id":"b","posted":"2026-08-02","hold_3s_rate":0.5,"completion_rate":0.6}]}', encoding="utf-8")
            failed = run_score(bad, temp / "constant-report")
            self.assertEqual(failed.returncode, 2)
            self.assertIn("non-standard numeric constant", failed.stderr)
            self.assertFalse((temp / "constant-report").exists())

    def test_single_metric_label_disjoint_slices_and_literal_playbook(self):
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            source = self.write_csv(temp, """id,posted,caption,hold_3s_rate,completion_rate,verified_audiovisual_opener,audiovisual_opener_verified
a,2026-08-01,"# Title",0.9,0.7,"- visual\n# next\t",true
b,2026-08-02,second,0.6,0.6,,
c,2026-08-03,third,0.3,0.5,,
""")
            one_metric = subprocess.run([sys.executable, str(SCRIPT), str(source), "--start", "2026-08-01", "--end", "2026-08-31", "--rank-metrics", "hold_3s_rate", "--top", "2", "--outdir", str(temp / "one-metric")], text=True, capture_output=True, check=False)
            self.assertEqual(one_metric.returncode, 0, one_metric.stderr)
            dashboard = (temp / "one-metric" / "dashboard.md").read_text(encoding="utf-8")
            self.assertIn("hold_3s_rate percentile", dashboard)
            self.assertNotIn("Heuristic composite percentile", dashboard)
            self.assertIn("Lowest 1 (disjoint from highest)", dashboard)
            with (temp / "one-metric" / "top10.csv").open(newline="", encoding="utf-8") as handle:
                top = list(csv.DictReader(handle))
            with (temp / "one-metric" / "bottom10.csv").open(newline="", encoding="utf-8") as handle:
                bottom = list(csv.DictReader(handle))
            self.assertEqual(top[0].keys() >= {"hold_3s_rate_percentile"}, True)
            self.assertFalse({row["id"] for row in top} & {row["id"] for row in bottom})
            playbook = (temp / "one-metric" / "hook_patterns.md").read_text(encoding="utf-8")
            self.assertIn("```\n# Title\n```", playbook)
            self.assertIn("```\n- visual\n# next⇥\n```", playbook)
            invalid = subprocess.run([sys.executable, str(SCRIPT), str(source), "--start", "2026-08-01", "--end", "2026-08-31", "--rank-metrics", "hold_3s_rate", "--composite", "--outdir", str(temp / "invalid-single")], text=True, capture_output=True, check=False)
            self.assertEqual(invalid.returncode, 2)
            self.assertIn("requires two or more", invalid.stderr)


if __name__ == "__main__":
    unittest.main()
