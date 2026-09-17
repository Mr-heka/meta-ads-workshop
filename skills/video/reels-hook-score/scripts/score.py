#!/usr/bin/env python3
# Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠
# Provenance marker: sk-pv8zap
"""Build a source-traceable, cohort-comparable Reels report (stdlib only)."""

import argparse
import csv
import datetime as dt
import hashlib
import io
import json
import math
import os
import re
import shutil
import stat
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path


class ValidationError(Exception):
    """An input or reporting contract violation."""


ALIASES = {
    "id": ("id", "reel_id", "media_id"),
    "posted": ("posted", "posted_date", "publish_date"),
    "caption": ("caption", "description", "text"),
    "url": ("url", "permalink"),
    "views": ("views", "plays"),
    "saves": ("saves",),
    "shares": ("shares",),
    "saves_per_view": ("saves_per_view",),
    "shares_per_view": ("shares_per_view",),
    "hold_3s_rate": ("hold_3s_rate",),
    "hold_15s_rate": ("hold_15s_rate",),
    "completion_rate": ("completion_rate",),
    "full_watch_rate": ("full_watch_rate",),
    "watch_ratio": ("watch_ratio",),
    "average_watch_seconds": ("average_watch_seconds",),
    "duration_seconds": ("duration_seconds",),
    "watches_per_viewer": ("watches_per_viewer",),
    "replays_per_viewer": ("replays_per_viewer",),
    "replays": ("replays",),
    "unique_viewers": ("unique_viewers",),
    "verified_audiovisual_opener": ("verified_audiovisual_opener",),
    "audiovisual_opener_verified": ("audiovisual_opener_verified",),
}
METRICS = (
    "hold_3s_rate", "hold_15s_rate", "completion_rate", "full_watch_rate",
    "watch_ratio", "saves_per_view", "shares_per_view", "watches_per_viewer",
    "replays_per_viewer",
)
RATE_METRICS = ("hold_3s_rate", "hold_15s_rate", "completion_rate", "full_watch_rate")
RATIO_METRICS = ("watch_ratio", "saves_per_view", "shares_per_view", "watches_per_viewer", "replays_per_viewer")
PATTERNS = (
    ("Contrarian command", re.compile(r"^\s*(stop|quit|never|don't|delete|forget|ignore)\b", re.I)),
    ("Question", re.compile(r"^\s*(why|how|what|when|who|which|can|do|is|are|have you|did you)\b.*\?", re.I)),
    ("Numbered claim", re.compile(r"\b\d+\s+(ways?|things?|tools?|mistakes?|reasons?|steps?|tips?|hacks?|signs?|lessons?|rules?)\b", re.I)),
    ("Discovery", re.compile(r"\b(i (just )?(found|discovered|built|tried|tested)|this (new )?(tool|app|ai|trick))\b", re.I)),
    ("Curiosity gap", re.compile(r"\b(nobody (talks about|tells you)|the secret|what no one|the real reason|most people (miss|don't know))\b", re.I)),
    ("How-to", re.compile(r"^\s*(how to|how i|here's how|the (easiest|fastest|simplest) way)\b", re.I)),
)
NUMBER = re.compile(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?\Z")


def fail(row_number, message):
    raise ValidationError("row {}: {}".format(row_number, message))


def input_value(row, field, row_number):
    """Read one documented alias; two aliases are an ambiguous mapping."""
    present = [key for key in ALIASES[field] if key in row and row[key] not in (None, "")]
    if len(present) > 1:
        fail(row_number, "ambiguous {} mapping: {}".format(field, ", ".join(present)))
    return row[present[0]] if present else None


def plain_text(value, field, row_number):
    if value is None:
        return None
    if not isinstance(value, str):
        fail(row_number, "{} must be a string".format(field))
    return value


def number(value, field, row_number, minimum=0.0, maximum=None, integer=False):
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        fail(row_number, "{} must be a finite decimal, not boolean".format(field))
    if integer:
        if isinstance(value, int):
            parsed = value
        elif isinstance(value, float):
            fail(row_number, "{} must be a JSON integer or exact decimal string count".format(field))
        elif isinstance(value, str):
            if not NUMBER.fullmatch(value.strip()):
                fail(row_number, "{} must be a plain normalized decimal (no percent, comma, or unit)".format(field))
            try:
                parsed_decimal = Decimal(value.strip())
            except InvalidOperation:
                fail(row_number, "{} must be an exact integer count".format(field))
            if not parsed_decimal.is_finite() or parsed_decimal != parsed_decimal.to_integral_value():
                fail(row_number, "{} must be an integer count".format(field))
            parsed = int(parsed_decimal)
        else:
            fail(row_number, "{} must be an exact integer count".format(field))
        if parsed < minimum or (maximum is not None and parsed > maximum):
            bounds = "{}..{}".format(minimum, maximum) if maximum is not None else ">={}".format(minimum)
            fail(row_number, "{} must be in {}".format(field, bounds))
        return parsed
    if isinstance(value, str):
        if not NUMBER.fullmatch(value.strip()):
            fail(row_number, "{} must be a plain normalized decimal (no percent, comma, or unit)".format(field))
        value = value.strip()
    elif not isinstance(value, (int, float)):
        fail(row_number, "{} must be a finite decimal".format(field))
    try:
        parsed = float(value)
    except (ValueError, OverflowError):
        fail(row_number, "{} is outside the supported finite numeric range".format(field))
    if not math.isfinite(parsed):
        fail(row_number, "{} must be finite".format(field))
    if parsed == 0 and Decimal(str(value)) != 0:
        fail(row_number, "{} underflows the supported numeric range".format(field))
    if parsed < minimum or (maximum is not None and parsed > maximum):
        bounds = "{}..{}".format(minimum, maximum) if maximum is not None else ">={}".format(minimum)
        fail(row_number, "{} must be in {}".format(field, bounds))
    return parsed


def bool_value(value, field, row_number):
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, str) and value.lower() in ("true", "false"):
        return value.lower() == "true"
    fail(row_number, "{} must be boolean true or false".format(field))


def iso_date(value, row_number):
    if value is None or value == "":
        return None
    if not isinstance(value, str) or not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
        fail(row_number, "posted must be an ISO YYYY-MM-DD string")
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        fail(row_number, "posted must be ISO YYYY-MM-DD")


def first_line(caption):
    if caption is None:
        return None
    return caption.splitlines()[0] if caption.splitlines() else ""


def load_input(path):
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValidationError("input must be UTF-8: {}".format(exc))
    if path.suffix.lower() == ".json":
        try:
            def no_duplicate_keys(pairs):
                parsed = {}
                for key, value in pairs:
                    if key in parsed:
                        raise ValidationError("JSON has duplicate key: {}".format(key))
                    parsed[key] = value
                return parsed
            def reject_constant(value):
                raise ValidationError("JSON contains non-standard numeric constant: {}".format(value))
            def finite_float(value):
                parsed = float(value)
                if not math.isfinite(parsed):
                    raise ValidationError("JSON number is outside the supported finite numeric range: {}".format(value))
                if parsed == 0 and Decimal(value) != 0:
                    raise ValidationError("JSON number underflows the supported numeric range: {}".format(value))
                return parsed
            data = json.loads(text, object_pairs_hook=no_duplicate_keys, parse_constant=reject_constant, parse_float=finite_float)
        except json.JSONDecodeError as exc:
            raise ValidationError("invalid JSON: {}".format(exc))
        wrapper = {"kind": "top_level_array", "container_key": None, "metadata": {}}
        if isinstance(data, dict):
            arrays = [key for key in ("reels", "items", "data", "results") if isinstance(data.get(key), list)]
            if len(arrays) != 1:
                raise ValidationError("JSON object must contain exactly one of reels, items, data, results arrays")
            container_key = arrays[0]
            wrapper = {"kind": "object_container", "container_key": container_key, "metadata": {key: value for key, value in data.items() if key != container_key}}
            data = data[container_key]
        if not isinstance(data, list) or not data:
            raise ValidationError("JSON input must be a non-empty array of reel objects")
        if any(not isinstance(row, dict) for row in data):
            raise ValidationError("JSON input contains a non-object row")
        return raw, data, "json", wrapper
    try:
        csv.field_size_limit(4 * 1024 * 1024)
        reader = csv.reader(io.StringIO(text))
        headers = next(reader, None)
        if not headers or any(not name for name in headers):
            raise ValidationError("CSV needs non-empty headers")
        if len(set(headers)) != len(headers):
            raise ValidationError("CSV has duplicate headers")
        rows = []
        for line_number, cells in enumerate(reader, start=2):
            if len(cells) != len(headers):
                raise ValidationError("CSV row {} has {} cells; expected {}".format(line_number, len(cells), len(headers)))
            rows.append(dict(zip(headers, cells)))
    except csv.Error as exc:
        raise ValidationError("invalid CSV: {}".format(exc))
    if not rows:
        raise ValidationError("CSV has no data rows")
    return raw, rows, "csv", {"kind": "csv", "container_key": None, "metadata": {}}


def finite_ratio(numerator, denominator, field, row_number):
    try:
        result = numerator / denominator
    except (OverflowError, ZeroDivisionError):
        fail(row_number, "{} is outside the supported finite numeric range".format(field))
    if not math.isfinite(result):
        fail(row_number, "{} must produce a finite ratio".format(field))
    if result == 0 and numerator != 0:
        fail(row_number, "{} underflows the supported numeric range".format(field))
    return result


def normalize_row(raw, row_number, start, end):
    identifier = plain_text(input_value(raw, "id", row_number), "id", row_number)
    if not identifier or not identifier.strip():
        fail(row_number, "id is required")
    posted = iso_date(input_value(raw, "posted", row_number), row_number)
    caption = plain_text(input_value(raw, "caption", row_number), "caption", row_number)
    url = plain_text(input_value(raw, "url", row_number), "url", row_number)
    values = {metric: number(input_value(raw, metric, row_number), metric, row_number, 0.0, 1.0) for metric in RATE_METRICS}
    values.update({metric: number(input_value(raw, metric, row_number), metric, row_number) for metric in RATIO_METRICS})
    views = number(input_value(raw, "views", row_number), "views", row_number, integer=True)
    saves = number(input_value(raw, "saves", row_number), "saves", row_number, integer=True)
    shares = number(input_value(raw, "shares", row_number), "shares", row_number, integer=True)
    replays = number(input_value(raw, "replays", row_number), "replays", row_number, integer=True)
    unique_viewers = number(input_value(raw, "unique_viewers", row_number), "unique_viewers", row_number, integer=True)
    if views == 0 and any(count is not None and count > 0 for count in (saves, shares)):
        fail(row_number, "zero views cannot have positive saves or shares")
    if unique_viewers == 0 and replays is not None and replays > 0:
        fail(row_number, "zero unique_viewers cannot have positive replays")
    for raw_count, ratio in ((saves, "saves_per_view"), (shares, "shares_per_view")):
        if raw_count is not None and values[ratio] is not None:
            fail(row_number, "{} and {} cannot both be supplied".format(ratio.replace("_per_view", ""), ratio))
        if raw_count is not None and views is not None and views > 0:
            values[ratio] = finite_ratio(raw_count, views, ratio, row_number)
    average = number(input_value(raw, "average_watch_seconds", row_number), "average_watch_seconds", row_number)
    duration = number(input_value(raw, "duration_seconds", row_number), "duration_seconds", row_number)
    if (average is None) != (duration is None):
        fail(row_number, "average_watch_seconds and duration_seconds must be supplied together")
    if average is not None:
        if duration <= 0:
            fail(row_number, "duration_seconds must be greater than zero")
        if values["watch_ratio"] is not None:
            fail(row_number, "watch_ratio and average_watch_seconds/duration_seconds cannot both be supplied")
        values["watch_ratio"] = finite_ratio(average, duration, "watch_ratio", row_number)
    if replays is not None and values["replays_per_viewer"] is not None:
        fail(row_number, "replays and replays_per_viewer cannot both be supplied")
    if replays is not None and unique_viewers is not None and unique_viewers > 0:
        values["replays_per_viewer"] = finite_ratio(replays, unique_viewers, "replays_per_viewer", row_number)
    audiovisual = plain_text(input_value(raw, "verified_audiovisual_opener", row_number), "verified_audiovisual_opener", row_number)
    audiovisual_verified = bool_value(input_value(raw, "audiovisual_opener_verified", row_number), "audiovisual_opener_verified", row_number)
    if audiovisual is not None and audiovisual_verified is not True:
        fail(row_number, "verified_audiovisual_opener requires audiovisual_opener_verified true")
    if audiovisual_verified is True and audiovisual is None:
        fail(row_number, "audiovisual_opener_verified true requires verified_audiovisual_opener")
    if posted is None:
        status = "missing_posted_not_ranked"
    elif start <= posted <= end:
        status = "in_cohort"
    else:
        status = "outside_cohort"
    sources = {metric: ("direct" if input_value(raw, metric, row_number) is not None else None) for metric in METRICS}
    if average is not None:
        sources["watch_ratio"] = "average_watch_seconds/duration_seconds"
    if saves is not None and views is not None and views > 0:
        sources["saves_per_view"] = "saves/views"
    if shares is not None and views is not None and views > 0:
        sources["shares_per_view"] = "shares/views"
    if replays is not None and unique_viewers is not None and unique_viewers > 0:
        sources["replays_per_viewer"] = "replays/unique_viewers"
    return {
        "id": identifier.strip(), "posted": posted.isoformat() if posted else None,
        "url": url, "caption": caption, "caption_opener_raw": first_line(caption),
        "verified_audiovisual_opener": audiovisual, "audiovisual_opener_verified": audiovisual_verified,
        "views": views, "saves": saves, "shares": shares, "replays": replays,
        "unique_viewers": unique_viewers, "metrics": values,
        "metric_sources": sources, "cohort_status": status, "raw": raw,
    }


def percentile(values, value):
    """Tie-aware 0..100 within the explicitly comparable eligible cohort."""
    less = sum(candidate < value for candidate in values)
    equal = sum(candidate == value for candidate in values)
    return 100.0 * (less + (equal - 1) / 2.0) / (len(values) - 1)


def score_rows(rows, metrics, composite):
    eligible = []
    for row in rows:
        missing = [metric for metric in metrics if row["metrics"][metric] is None]
        row["rank_missing_metrics"] = missing
        row["rank"] = None
        row["cohort_score"] = None
        row["metric_percentiles"] = None
        if row["cohort_status"] == "in_cohort" and not missing:
            eligible.append(row)
    if len(eligible) < 2:
        raise ValidationError("fewer than two in-cohort rows share the requested metric basis")
    distributions = {metric: [row["metrics"][metric] for row in eligible] for metric in metrics}
    for row in eligible:
        percents = {metric: percentile(distributions[metric], row["metrics"][metric]) for metric in metrics}
        row["metric_percentiles"] = percents
        row["cohort_score"] = sum(percents.values()) / len(metrics) if composite else percents[metrics[0]]
    eligible.sort(key=lambda row: (-row["cohort_score"], row["id"]))
    for position, row in enumerate(eligible, start=1):
        row["rank"] = 1 + sum(other["cohort_score"] > row["cohort_score"] for other in eligible)
        row["display_order"] = position
    return eligible


def md(value, limit=320):
    if value is None or value == "":
        return "n/a"
    text = str(value)
    if len(text) > limit:
        text = text[:limit] + " … [display truncated; see normalized.json]"
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("`", "\\`").replace("*", "\\*").replace("_", "\\_").replace("[", "\\[").replace("]", "\\]").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>")


def code_literal(value, limit=320):
    """Render user text as a fenced display excerpt, never active Markdown."""
    if value is None or value == "":
        text = "n/a"
    else:
        text = str(value)
        if len(text) > limit:
            text = text[:limit] + " … [display truncated; see normalized.json]"
    displayed = []
    for character in text:
        if character == "\t":
            displayed.append("⇥")
        elif character == "\r":
            displayed.append("␍")
        elif ord(character) < 32 and character != "\n":
            displayed.append("\\u{:04x}".format(ord(character)))
        else:
            displayed.append(character)
    text = "".join(displayed)
    longest_ticks = max([len(run) for run in re.findall(r"`+", text)] or [0])
    fence = "`" * max(3, longest_ticks + 1)
    return "{}\n{}\n{}".format(fence, text, fence)


def csv_cell(value):
    if value is None:
        return ""
    text = str(value)
    visible = text.lstrip(" \t\r\n")
    return "'" + text if text[:1] in ("\t", "\r", "\n") or visible[:1] in ("=", "+", "-", "@") else text


def fixed(value, digits=3):
    return "n/a" if value is None else ("{:.%df}" % digits).format(value)


def score_label(metrics, composite):
    return "Heuristic composite percentile" if composite else "{} percentile".format(metrics[0])


def row_table(rows, metrics, composite):
    if not rows:
        return "_none_"
    lines = ["| Rank | Caption opener display excerpt (raw source in normalized.json) | Verified audiovisual opener display excerpt | {} | {} |".format(score_label(metrics, composite), " | ".join(metrics)), "|---:|---|---|---:|" + "---:|" * len(metrics)]
    for row in rows:
        metric_values = " | ".join(fixed(row["metrics"][metric]) for metric in metrics)
        lines.append("| {} | {} | {} | {} | {} |".format(row["rank"], md(row["caption_opener_raw"]), md(row["verified_audiovisual_opener"]), fixed(row["cohort_score"], 1), metric_values))
    return "\n".join(lines)


def coverage_table(rows, cap):
    lines = ["| ID | Status | Missing selected metrics | Caption opener |", "|---|---|---|---|"]
    unranked = [row for row in rows if row["rank"] is None]
    for row in unranked[:cap]:
        missing = ", ".join(row["rank_missing_metrics"]) or "n/a"
        lines.append("| {} | {} | {} | {} |".format(md(row["id"]), row["cohort_status"], md(missing), md(row["caption_opener_raw"])))
    if len(unranked) > cap:
        lines.append("\n_{} additional unranked or out-of-cohort rows are retained in normalized.json._".format(len(unranked) - cap))
    return "\n".join(lines) if unranked else "_all in-cohort rows were ranked_"


def pattern_block(rows):
    counts = {name: 0 for name, _ in PATTERNS}
    for row in rows:
        opener = row["caption_opener_raw"] or ""
        for name, expression in PATTERNS:
            if expression.search(opener):
                counts[name] += 1
    found = ["- {}: {} ranked caption opener(s)".format(name, count) for name, count in counts.items() if count]
    return "\n".join(found) if found else "_No configured descriptive labels matched ranked caption openers._"


def write_rank_csv(path, rows, metrics, composite):
    columns = ["rank", "id", "posted", "url", "caption_opener", "verified_audiovisual_opener", "heuristic_composite_percentile" if composite else "{}_percentile".format(metrics[0])] + list(metrics)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(columns)
        for row in rows:
            writer.writerow([row["rank"], csv_cell(row["id"]), row["posted"], csv_cell(row["url"]), csv_cell(row["caption_opener_raw"]), csv_cell(row["verified_audiovisual_opener"]), fixed(row["cohort_score"], 3)] + [fixed(row["metrics"][metric], 6) for metric in metrics])


def write_playbook(path, rows):
    lines = ["# Caption-opener playbook", "", "These are display excerpts of exact source caption first lines; full raw text is retained in normalized.json. They are not inferred audiovisual openers.", ""]
    for row in rows:
        labels = [name for name, expression in PATTERNS if expression.search(row["caption_opener_raw"] or "")]
        lines.extend(["## {}. Caption opener display excerpt".format(row["rank"]), code_literal(row["caption_opener_raw"]), "", "Verified audiovisual opener display excerpt:", code_literal(row["verified_audiovisual_opener"]), "", "Descriptive labels: {}".format(", ".join(labels) if labels else "none"), ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def render_dashboard(template, context):
    return re.sub(r"\{(start|end|source_name|source_sha256|scope|ranked_rows|coverage_rows|patterns|limits)\}", lambda match: str(context[match.group(1)]), template)


def parse_metrics(value):
    metrics = tuple(part.strip() for part in value.split(",") if part.strip())
    if not metrics:
        raise ValidationError("--rank-metrics needs at least one metric")
    if len(set(metrics)) != len(metrics) or any(metric not in METRICS for metric in metrics):
        raise ValidationError("--rank-metrics must be unique supported normalized metrics: {}".format(", ".join(METRICS)))
    return metrics


def ignored_fields(raw_rows):
    known = {alias for aliases in ALIASES.values() for alias in aliases}
    return sorted({key for row in raw_rows for key in row if key not in known})


def reserve_output_directory(outdir):
    """Atomically claim an absent directory; never replace another creator's output."""
    outdir.parent.mkdir(parents=True, exist_ok=True)
    try:
        os.mkdir(outdir)
    except FileExistsError:
        raise ValidationError("output directory already exists or was created concurrently: {}".format(outdir))
    stat = outdir.stat()
    return (stat.st_dev, stat.st_ino)


def assert_owned(outdir, ownership):
    directory = os.lstat(outdir)
    if not stat.S_ISDIR(directory.st_mode):
        raise ValidationError("output directory became a non-directory or symlink during publication")
    if (directory.st_dev, directory.st_ino) != ownership:
        raise ValidationError("output directory ownership changed during publication")


def publish_reserved(outdir, ownership, files):
    """Create files under an owned reservation without replacing file targets."""
    stage = outdir / ".building"
    try:
        assert_owned(outdir, ownership)
        stage.mkdir()
        for name, data in files.items():
            target = stage / name
            if isinstance(data, bytes):
                target.write_bytes(data)
            else:
                target.write_text(data, encoding="utf-8")
        for name in files:
            assert_owned(outdir, ownership)
            target = outdir / name
            try:
                os.link(stage / name, target, follow_symlinks=False)
            except FileExistsError:
                raise ValidationError("reserved output already contains {}".format(name))
            (stage / name).unlink()
        stage.rmdir()
    except Exception as exc:
        if stage.exists():
            shutil.rmtree(stage, ignore_errors=True)
        write_failure_receipt(outdir, ownership, exc)
        raise


def write_failure_receipt(outdir, ownership, error):
    try:
        assert_owned(outdir, ownership)
        descriptor = os.open(outdir / "FAILED.json", os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            json.dump({"status": "failed", "error": str(error), "reservation": {"device": ownership[0], "inode": ownership[1]}}, handle, indent=2)
            handle.write("\n")
    except Exception:
        pass


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build a local, comparable Reels cohort report from CSV or JSON.")
    parser.add_argument("input", help="UTF-8 CSV or JSON export")
    parser.add_argument("--start", required=True, help="inclusive cohort start, YYYY-MM-DD")
    parser.add_argument("--end", required=True, help="inclusive cohort end, YYYY-MM-DD")
    parser.add_argument("--rank-metrics", required=True, help="comma-separated normalized metrics")
    parser.add_argument("--composite", action="store_true", help="acknowledge a multi-metric percentile mean as heuristic")
    parser.add_argument("--top", type=int, default=10, help="top and bottom row count (default 10)")
    parser.add_argument("--outdir", required=True, help="new output directory; must not already exist")
    args = parser.parse_args(argv)
    if not all(re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value) for value in (args.start, args.end)):
        raise ValidationError("--start and --end must be ISO YYYY-MM-DD")
    try:
        start, end = dt.date.fromisoformat(args.start), dt.date.fromisoformat(args.end)
    except ValueError:
        raise ValidationError("--start and --end must be ISO YYYY-MM-DD")
    if end < start:
        raise ValidationError("--end must be on or after --start")
    if args.top < 1 or args.top > 50:
        raise ValidationError("--top must be between one and 50 to keep rendered reports bounded")
    metrics = parse_metrics(args.rank_metrics)
    if len(metrics) > 1 and not args.composite:
        raise ValidationError("multiple --rank-metrics require --composite; that composite is explicitly heuristic")
    if len(metrics) == 1 and args.composite:
        raise ValidationError("--composite requires two or more --rank-metrics; one metric uses its percentile directly")
    input_path = Path(args.input).expanduser()
    outdir = Path(args.outdir).expanduser()
    if not input_path.is_file():
        raise ValidationError("input file does not exist: {}".format(input_path))
    raw_bytes, raw_rows, input_format, container = load_input(input_path)
    rows = [normalize_row(raw, index, start, end) for index, raw in enumerate(raw_rows, start=2 if input_format == "csv" else 0)]
    identifiers = set()
    for row in rows:
        if row["id"] in identifiers:
            raise ValidationError("duplicate id: {}".format(row["id"]))
        identifiers.add(row["id"])
    ranked = score_rows(rows, metrics, args.composite)
    top = ranked[:args.top]
    bottom = ranked[len(top):] if len(ranked) <= 2 * args.top else ranked[-args.top:]
    template_path = Path(__file__).resolve().parent.parent / "templates" / "dashboard.md.j2"
    template = template_path.read_text(encoding="utf-8")
    source_hash = hashlib.sha256(raw_bytes).hexdigest()
    ignored = sorted(set(ignored_fields(raw_rows) + list(container["metadata"])))
    scope = "Inclusive posted-date cohort: {} to {}. {} source rows; {} in cohort; {} ranked on the shared metric basis `{}`.".format(start, end, len(rows), sum(row["cohort_status"] == "in_cohort" for row in rows), len(ranked), ", ".join(metrics))
    if len(metrics) > 1:
        scope += " Score is an unweighted percentile-mean heuristic, not a validated predictor or action recommendation."
    if ignored:
        scope += " Ignored source fields are recorded in provenance.json: {}.".format(", ".join(md(field, 80) for field in ignored[:20]))
        if len(ignored) > 20:
            scope += " ({} more)".format(len(ignored) - 20)
    ranked_display = "### Highest {}\n\n{}".format(len(top), row_table(top, metrics, args.composite))
    if bottom:
        ranked_display += "\n\n### Lowest {} (disjoint from highest)\n\n{}".format(len(bottom), row_table(bottom, metrics, args.composite))
    limits = "Missing values remain missing. Rows outside the date window, without a posting date, or without every selected metric are not ranked. Caption patterns are descriptive only. Values have no paid, archive, repost, or causal recommendation. Cohort size: {}; tied scores receive the same competition rank, while display order is deterministic by ID. Dashboard tables are capped; complete source evidence remains in input.raw and normalized.json.".format(len(ranked))
    context = {
        "start": start, "end": end, "source_name": md(input_path.name), "source_sha256": source_hash,
        "scope": scope, "ranked_rows": ranked_display, "coverage_rows": coverage_table(rows, args.top * 2),
        "patterns": pattern_block(ranked), "limits": limits,
    }
    normalized = {"schema_version": 5, "cohort": {"start": start.isoformat(), "end": end.isoformat()}, "rank_metrics": metrics, "composite_heuristic": args.composite, "rows": rows}
    provenance = {"schema_version": 5, "input": {"path": str(input_path.resolve()), "format": input_format, "sha256": source_hash, "bytes": len(raw_bytes), "container": container, "ignored_source_fields": ignored}, "cohort": {"start": start.isoformat(), "end": end.isoformat()}, "rank_metrics": metrics, "composite_heuristic": args.composite, "normalization": {"rate_unit": "fraction 0..1", "per_view_unit": "non-negative event ratio, unbounded", "count_unit": "non-negative exact integer count", "watch_ratio_derivation": "average_watch_seconds/duration_seconds, may exceed 1", "replays_per_viewer_derivation": "replays/unique_viewers when both supplied", "watches_per_viewer": "direct source field only", "caption_opener": "exact first caption line", "audiovisual_opener": "only source supplied and explicitly verified"}}
    dashboard = render_dashboard(template, context)
    if len(dashboard.encode("utf-8")) > 200 * 1024:
        raise ValidationError("rendered dashboard exceeds 200 KB despite display caps")
    csv_files = {}
    reservation = reserve_output_directory(outdir)
    try:
        csv_stage = outdir / ".csv-build"
        csv_stage.mkdir()
        write_rank_csv(csv_stage / "top10.csv", top, metrics, args.composite)
        write_rank_csv(csv_stage / "bottom10.csv", bottom, metrics, args.composite)
        write_playbook(csv_stage / "hook_patterns.md", top)
        csv_files = {name: (csv_stage / name).read_text(encoding="utf-8") for name in ("top10.csv", "bottom10.csv", "hook_patterns.md")}
        shutil.rmtree(csv_stage)
        publish_reserved(outdir, reservation, {
            "input.raw": raw_bytes,
            "normalized.json": json.dumps(normalized, indent=2, ensure_ascii=False, allow_nan=False) + "\n",
            "provenance.json": json.dumps(provenance, indent=2, ensure_ascii=False, allow_nan=False) + "\n",
            "dashboard.md": dashboard,
            **csv_files,
        })
    except Exception:
        if csv_stage.exists():
            shutil.rmtree(csv_stage, ignore_errors=True)
        write_failure_receipt(outdir, reservation, sys.exc_info()[1])
        raise
    print("Scored {} comparable in-cohort records. Output: {}".format(len(ranked), outdir))


if __name__ == "__main__":
    try:
        main()
    except (ValidationError, OSError) as exc:
        print("ERROR: {}".format(exc), file=sys.stderr)
        sys.exit(2)
