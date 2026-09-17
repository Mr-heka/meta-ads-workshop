# Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠
# Provenance marker: sk-2onwkn
from __future__ import annotations

import importlib.util
import json
import os
from decimal import Decimal, localcontext
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "metrics.py"
spec = importlib.util.spec_from_file_location("paid_ads_metrics", SCRIPT)
assert spec and spec.loader
metrics = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = metrics
spec.loader.exec_module(metrics)


def supplied(**overrides):
    data = {
        "currency": "AUD",
        "period": "2026-09-01 to 2026-09-05",
        "source": "fictional local export",
        "spend": Decimal("100"),
        "revenue": Decimal("250"),
        "conversions": 4,
        "leads": 10,
        "impressions": 1000,
        "clicks": 50,
        "margin_pct": Decimal("50"),
    }
    data.update(overrides)
    return data


class CalculateTests(unittest.TestCase):
    def test_known_example_and_fixed_schema(self):
        result = metrics.calculate(supplied())
        self.assertEqual(result["input"]["spend"], "100")
        self.assertEqual(result["metrics"]["roas"]["value"], "2.5")
        self.assertEqual(result["metrics"]["cpa"]["value"], "25")
        self.assertEqual(result["metrics"]["cpm"]["value"], "100")
        self.assertEqual(result["metrics"]["ctr_pct"]["value"], "5")
        self.assertEqual(set(result["metrics"]), {
            "roas", "cpa", "cpl", "cpc", "cpm", "ctr_pct", "conversion_rate_pct",
            "lead_capture_rate_pct", "lead_to_conversion_rate_pct", "revenue_per_conversion",
            "break_even_roas", "contribution_after_ads", "revenue_to_break_even", "revenue_gap_to_break_even",
        })
        for record in result["metrics"].values():
            self.assertEqual(set(record), {"value", "unit", "formula", "unavailable_reason"})

    def test_missing_and_known_zero_remain_distinct(self):
        result = metrics.calculate(supplied(revenue=None, conversions=0, clicks=0, margin_pct=None))
        self.assertIsNone(result["input"]["revenue"])
        self.assertEqual(result["input"]["conversions"], 0)
        self.assertEqual(result["metrics"]["roas"]["unavailable_reason"], "missing_input")
        self.assertEqual(result["metrics"]["cpa"]["unavailable_reason"], "zero_denominator")
        self.assertEqual(result["metrics"]["cpc"]["unavailable_reason"], "zero_denominator")
        self.assertEqual(result["metrics"]["break_even_roas"]["unavailable_reason"], "missing_input")

    def test_independent_denominators_and_zero_values(self):
        result = metrics.calculate(supplied(impressions=None, clicks=10, conversions=0, leads=0, revenue=Decimal("0")))
        self.assertEqual(result["metrics"]["cpc"]["value"], "10")
        self.assertEqual(result["metrics"]["cpm"]["unavailable_reason"], "missing_input")
        self.assertEqual(result["metrics"]["ctr_pct"]["unavailable_reason"], "missing_input")
        self.assertEqual(result["metrics"]["conversion_rate_pct"]["value"], "0")
        self.assertEqual(result["metrics"]["lead_capture_rate_pct"]["value"], "0")
        self.assertEqual(result["metrics"]["roas"]["value"], "0")

    def test_zero_spend_margin_and_clicks_do_not_crash(self):
        result = metrics.calculate(supplied(spend=Decimal("0"), revenue=Decimal("10"), clicks=0, margin_pct=Decimal("0")))
        self.assertEqual(result["metrics"]["roas"]["unavailable_reason"], "zero_denominator")
        self.assertEqual(result["metrics"]["break_even_roas"]["unavailable_reason"], "zero_denominator")
        self.assertEqual(result["metrics"]["revenue_to_break_even"]["unavailable_reason"], "zero_denominator")
        self.assertEqual(result["metrics"]["revenue_gap_to_break_even"]["unavailable_reason"], "zero_denominator")

    def test_decimal_rounding_and_contribution_gap_are_distinct(self):
        rounded = metrics.calculate(supplied(spend=Decimal("1"), clicks=3, revenue=Decimal("100"), conversions=1, margin_pct=Decimal("50")))
        self.assertEqual(rounded["metrics"]["cpc"]["value"], "0.333333")
        distinction = metrics.calculate(supplied(spend=Decimal("100"), revenue=Decimal("100"), margin_pct=Decimal("50")))
        self.assertEqual(distinction["metrics"]["contribution_after_ads"]["value"], "-50")
        self.assertEqual(distinction["metrics"]["revenue_to_break_even"]["value"], "200")
        self.assertEqual(distinction["metrics"]["revenue_gap_to_break_even"]["value"], "100")
        self.assertIn("not net profit", distinction["metadata"]["contribution_assumption"])

    def test_ambient_decimal_context_does_not_change_arithmetic(self):
        with localcontext() as context:
            context.prec = 6
            result = metrics.calculate(supplied(spend=1, revenue=Decimal("123456789.12"), margin_pct=50))
        self.assertEqual(result["metrics"]["contribution_after_ads"]["value"], "61728393.56")

    def test_small_margin_large_ratio_and_numeric_bounds(self):
        result = metrics.calculate(supplied(spend=Decimal("1000000000000000"), revenue=0, margin_pct=Decimal("0.000000000001")))
        self.assertEqual(result["metrics"]["revenue_gap_to_break_even"]["value"], "100000000000000000000000000000")
        for value in [Decimal("1e-13"), Decimal("1e-1000000")]:
            with self.assertRaises(metrics.ValidationError):
                metrics.calculate(supplied(spend=value))

    def test_rates_over_100_are_preserved_with_caution(self):
        result = metrics.calculate(supplied(clicks=1, impressions=1, leads=3, conversions=4))
        self.assertEqual(result["metrics"]["conversion_rate_pct"]["value"], "400")
        self.assertEqual(result["metrics"]["lead_capture_rate_pct"]["value"], "300")
        self.assertIn("confirm_cohort_consistency", [c["code"] for c in result["metadata"]["cautions"]])

    def test_cohort_caution_uses_exact_counts_before_rounding(self):
        result = metrics.calculate(supplied(conversions=10**12, clicks=10**12 - 1, leads=None, impressions=None))
        self.assertEqual(result["metrics"]["conversion_rate_pct"]["value"], "100")
        self.assertIn("confirm_cohort_consistency", [c["code"] for c in result["metadata"]["cautions"]])

    def test_validation_rejects_invalid_types_and_bounds(self):
        invalid = [
            supplied(spend=True),
            supplied(spend="100"),
            supplied(spend=Decimal("-1")),
            supplied(revenue=Decimal("NaN")),
            supplied(clicks=-1),
            supplied(clicks=1.0),
            supplied(currency="auD"),
            supplied(period=""),
            supplied(margin_pct=Decimal("100.01")),
        ]
        for data in invalid:
            with self.subTest(data=data):
                with self.assertRaises(metrics.ValidationError):
                    metrics.calculate(data)
        unknown = supplied()
        unknown["campaign"] = "fictional"
        with self.assertRaises(metrics.ValidationError):
            metrics.calculate(unknown)


class CliTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, "-B", str(SCRIPT), *args], text=True, capture_output=True, check=False, timeout=5)

    def write_json(self, directory: Path, payload: str, name="input.json") -> Path:
        path = directory / name
        path.write_text(payload, encoding="utf-8")
        return path

    def test_cli_emits_strict_json_for_supplied_file(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = self.write_json(Path(temporary), json.dumps({
                "currency": "AUD", "period": "fictional period", "source": "fictional source",
                "spend": 0, "revenue": 0, "conversions": 0, "leads": 0,
                "impressions": 0, "clicks": 0, "margin_pct": 50,
            }))
            completed = self.run_cli("--file", str(path))
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(completed.stderr, "")
        output = json.loads(completed.stdout)
        self.assertEqual(output["input"]["spend"], "0")
        self.assertEqual(output["metrics"]["roas"]["unavailable_reason"], "zero_denominator")

    def test_cli_rejects_missing_duplicate_nonfinite_and_unknown_without_demo(self):
        missing = self.run_cli()
        self.assertNotEqual(missing.returncode, 0)
        self.assertEqual(missing.stdout, "")
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            cases = [
                '{"currency":"AUD","currency":"USD","period":"p","source":"s","spend":1}',
                '{"currency":"AUD","period":"p","source":"s","spend":NaN}',
                '{"currency":"AUD","period":"p","source":"s","spend":1,"unknown":2}',
            ]
            for index, payload in enumerate(cases):
                completed = self.run_cli("--file", str(self.write_json(root, payload, f"bad-{index}.json")))
                self.assertNotEqual(completed.returncode, 0)
                self.assertEqual(completed.stdout, "")
                self.assertTrue(completed.stderr.startswith("error:"))

    def test_cli_reports_extreme_numbers_deep_json_and_missing_file(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            payloads = [
                '{"currency":"AUD","period":"p","source":"s","spend":1e-1000000}',
                '{"currency":"AUD","period":"p","source":"s","spend":1e9999999999999999999}',
                '{"currency":"AUD","period":"p","source":"s","spend":' + '1' * 5000 + '}',
                '[' * 2000 + '0' + ']' * 2000,
            ]
            for index, payload in enumerate(payloads):
                result = self.run_cli("--file", str(self.write_json(root, payload, f"extreme-{index}.json")))
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertTrue(result.stderr.startswith("error:"), result.stderr)
                self.assertNotIn("Traceback", result.stderr)
            missing = self.run_cli("--file", str(root / "absent.json"))
            self.assertNotEqual(missing.returncode, 0)
            self.assertTrue(missing.stderr.startswith("error:"))

    def test_cli_refuses_symlink_special_and_oversized_inputs(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            target = self.write_json(root, '{"currency":"AUD","period":"p","source":"s","spend":1}')
            symlink = root / "link.json"
            symlink.symlink_to(target)
            linked = self.run_cli("--file", str(symlink))
            self.assertNotEqual(linked.returncode, 0)
            self.assertEqual(linked.stdout, "")
            self.assertIn("symlink", linked.stderr)

            fifo = root / "input.fifo"
            os.mkfifo(fifo)
            special = self.run_cli("--file", str(fifo))
            self.assertNotEqual(special.returncode, 0)
            self.assertEqual(special.stdout, "")
            self.assertIn("regular file", special.stderr)

            oversized = root / "oversized.json"
            oversized.write_bytes(b" " * (1024 * 1024 + 1))
            too_big = self.run_cli("--file", str(oversized))
            self.assertNotEqual(too_big.returncode, 0)
            self.assertEqual(too_big.stdout, "")
            self.assertIn("1 MiB", too_big.stderr)


if __name__ == "__main__":
    unittest.main()
