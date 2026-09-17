#!/usr/bin/env python3
# Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠
# Provenance marker: sk-2onwkn
"""Offline paid-ads metrics calculator for supplied observations only."""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import stat
import sys
from decimal import Context, Decimal, InvalidOperation, ROUND_HALF_UP, localcontext
from pathlib import Path
from typing import Any

MAX_INPUT_BYTES = 1024 * 1024
MAX_MONEY = Decimal("1000000000000000")
MAX_COUNT = 10**12
MONEY_KEYS = ("spend", "revenue")
COUNT_KEYS = ("conversions", "leads", "impressions", "clicks")
OPTIONAL_KEYS = ("revenue", "conversions", "leads", "impressions", "clicks", "margin_pct")
REQUIRED_KEYS = ("currency", "period", "source", "spend")
ALLOWED_KEYS = frozenset(REQUIRED_KEYS + OPTIONAL_KEYS)
CURRENCY_RE = re.compile(r"^[A-Z]{3}$", re.ASCII)
SIX_DECIMAL_PLACES = Decimal("0.000001")


class ValidationError(ValueError):
    """Raised when supplied calculator data is outside the fixed contract."""


def _decimal(value: Any, field: str, *, maximum: Decimal | None = None) -> Decimal:
    if isinstance(value, bool) or not isinstance(value, (int, float, Decimal)):
        raise ValidationError(f"{field} must be a JSON number")
    if isinstance(value, float) and not math.isfinite(value):
        raise ValidationError(f"{field} must be finite")
    try:
        number = value if isinstance(value, Decimal) else Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise ValidationError(f"{field} must be a finite number") from exc
    if not number.is_finite():
        raise ValidationError(f"{field} must be finite")
    if number < 0:
        raise ValidationError(f"{field} must be nonnegative")
    if maximum is not None and number > maximum:
        raise ValidationError(f"{field} exceeds the implementation limit")
    if number.as_tuple().exponent < -12 or len(number.as_tuple().digits) > 32:
        raise ValidationError(f"{field} exceeds 12 decimal places or 32 significant digits")
    return number


def _count(value: Any, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValidationError(f"{field} must be a nonnegative integer")
    if value < 0:
        raise ValidationError(f"{field} must be nonnegative")
    if value > MAX_COUNT:
        raise ValidationError(f"{field} exceeds the implementation limit")
    return value


def _plain_decimal(value: Decimal) -> str:
    if value == 0:
        return "0"
    return format(value, "f")


def _rounded_decimal(value: Decimal) -> str:
    rounded = value.quantize(SIX_DECIMAL_PLACES, rounding=ROUND_HALF_UP)
    if rounded == 0:
        return "0"
    return format(rounded, "f").rstrip("0").rstrip(".")


def validate(data: Any) -> dict[str, Any]:
    """Validate and normalize supplied data without reading external state."""
    if not isinstance(data, dict):
        raise ValidationError("input root must be a JSON object")

    unknown = set(data) - ALLOWED_KEYS
    if unknown:
        raise ValidationError(f"unknown field(s): {', '.join(sorted(unknown))}")
    missing = [key for key in REQUIRED_KEYS if key not in data]
    if missing:
        raise ValidationError(f"missing required field(s): {', '.join(missing)}")

    currency = data["currency"]
    if not isinstance(currency, str) or not CURRENCY_RE.fullmatch(currency):
        raise ValidationError("currency must be exactly three uppercase ASCII letters")

    normalized: dict[str, Any] = {"currency": currency}
    for field, limit in (("period", 200), ("source", 500)):
        value = data[field]
        if not isinstance(value, str) or value == "" or len(value) > limit:
            raise ValidationError(f"{field} must be a nonempty string of at most {limit} characters")
        normalized[field] = value

    normalized["spend"] = _decimal(data["spend"], "spend", maximum=MAX_MONEY)
    for field in MONEY_KEYS:
        if field == "spend":
            continue
        value = data.get(field)
        normalized[field] = None if value is None else _decimal(value, field, maximum=MAX_MONEY)
    for field in COUNT_KEYS:
        value = data.get(field)
        normalized[field] = None if value is None else _count(value, field)

    margin = data.get("margin_pct")
    normalized["margin_pct"] = None if margin is None else _decimal(margin, "margin_pct", maximum=Decimal("100"))
    return normalized


def _metric(
    value: Decimal | None,
    unit: str,
    formula: str,
    unavailable_reason: str | None = None,
) -> dict[str, str | None]:
    return {
        "value": None if value is None else _rounded_decimal(value),
        "unit": unit,
        "formula": formula,
        "unavailable_reason": unavailable_reason,
    }


def _ratio(
    numerator: Decimal | int | None,
    denominator: Decimal | int | None,
    unit: str,
    formula: str,
    multiplier: Decimal = Decimal("1"),
) -> dict[str, str | None]:
    if numerator is None or denominator is None:
        return _metric(None, unit, formula, "missing_input")
    if denominator == 0:
        return _metric(None, unit, formula, "zero_denominator")
    with localcontext() as context:
        context.prec = 50
        return _metric(Decimal(numerator) * multiplier / Decimal(denominator), unit, formula)


def calculate(data: Any) -> dict[str, Any]:
    """Return deterministic metrics for validated supplied observations."""
    with localcontext(Context(prec=64, rounding=ROUND_HALF_UP)):
        return _calculate(data)


def _calculate(data: Any) -> dict[str, Any]:
    values = validate(data)
    spend = values["spend"]
    revenue = values["revenue"]
    conversions = values["conversions"]
    leads = values["leads"]
    impressions = values["impressions"]
    clicks = values["clicks"]
    margin = values["margin_pct"]

    metrics = {
        "roas": _ratio(revenue, spend, "multiple", "revenue / spend"),
        "cpa": _ratio(spend, conversions, "currency_per_conversion", "spend / conversions"),
        "cpl": _ratio(spend, leads, "currency_per_lead", "spend / leads"),
        "cpc": _ratio(spend, clicks, "currency_per_click", "spend / clicks"),
        "cpm": _ratio(spend, impressions, "currency_per_1000_impressions", "spend / impressions * 1000", Decimal("1000")),
        "ctr_pct": _ratio(clicks, impressions, "percent", "clicks / impressions * 100", Decimal("100")),
        "conversion_rate_pct": _ratio(conversions, clicks, "percent", "conversions / clicks * 100", Decimal("100")),
        "lead_capture_rate_pct": _ratio(leads, clicks, "percent", "leads / clicks * 100", Decimal("100")),
        "lead_to_conversion_rate_pct": _ratio(conversions, leads, "percent", "conversions / leads * 100", Decimal("100")),
        "revenue_per_conversion": _ratio(revenue, conversions, "currency_per_conversion", "revenue / conversions"),
        "break_even_roas": _ratio(Decimal("100"), margin, "multiple", "100 / margin_pct"),
        "contribution_after_ads": _metric(
            None if revenue is None or margin is None else revenue * margin / Decimal("100") - spend,
            "currency",
            "revenue * margin_pct / 100 - spend",
            "missing_input" if revenue is None or margin is None else None,
        ),
        "revenue_to_break_even": _ratio(spend * Decimal("100"), margin, "currency", "spend * 100 / margin_pct"),
        "revenue_gap_to_break_even": _metric(
            None,
            "currency",
            "revenue_to_break_even - revenue",
            "missing_input" if revenue is None or margin is None else "zero_denominator" if margin == 0 else None,
        ),
    }
    if revenue is not None and margin is not None and margin != 0:
        with localcontext() as context:
            context.prec = 50
            revenue_to_break_even = spend * Decimal("100") / margin
        metrics["revenue_gap_to_break_even"] = _metric(
            revenue_to_break_even - revenue,
            "currency",
            "revenue_to_break_even - revenue",
        )

    cautions = [
        {
            "code": "supplied_data_unverified",
            "message": "Attribution and period are supplied observations and are not independently verified.",
        }
    ]
    rate_counts = ((clicks, impressions), (conversions, clicks), (leads, clicks), (conversions, leads))
    if any(
        numerator is not None and denominator is not None and denominator > 0 and numerator > denominator
        for numerator, denominator in rate_counts
    ):
        cautions.append(
            {
                "code": "confirm_cohort_consistency",
                "message": "Rates above 100 percent are retained because aggregates can include multiple events per click or different cohorts; confirm cohort consistency.",
            }
        )

    normalized_input = {
        "currency": values["currency"],
        "period": values["period"],
        "source": values["source"],
        "spend": _plain_decimal(spend),
        "revenue": None if revenue is None else _plain_decimal(revenue),
        "conversions": conversions,
        "leads": leads,
        "impressions": impressions,
        "clicks": clicks,
        "margin_pct": None if margin is None else _plain_decimal(margin),
    }
    return {
        "input": normalized_input,
        "metadata": {
            "numeric_encoding": "Monetary values, margin_pct, and metric values are decimal strings; counts are integers; null means unknown.",
            "scope": "Calculated from supplied observations only; not attribution proof, business profit certification, or permission to spend.",
            "contribution_assumption": "supplied margin_pct excludes ad spend and other omitted costs; contribution_after_ads is not net profit.",
            "cautions": cautions,
        },
        "metrics": metrics,
    }


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValidationError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_nonfinite(token: str) -> None:
    raise ValidationError(f"nonfinite JSON number: {token}")


def _parse_decimal_token(token: str) -> Decimal:
    if len(token) > 128:
        raise ValidationError("numeric token exceeds 128 characters")
    try:
        value = Decimal(token)
    except InvalidOperation as exc:
        raise ValidationError("invalid decimal token") from exc
    return _decimal(value, "numeric value", maximum=MAX_MONEY)


def _parse_integer_token(token: str) -> int:
    if len(token) > 32:
        raise ValidationError("integer token exceeds 32 characters")
    return int(token)


def _read_json_file(path_text: str) -> dict[str, Any]:
    path = Path(path_text)
    try:
        before = os.lstat(path)
    except OSError as exc:
        raise ValidationError(f"cannot inspect input file: {exc.strerror or exc}") from exc
    if stat.S_ISLNK(before.st_mode):
        raise ValidationError("input file must not be a symlink")
    if not stat.S_ISREG(before.st_mode):
        raise ValidationError("input file must be a regular file")
    if before.st_size > MAX_INPUT_BYTES:
        raise ValidationError("input file exceeds 1 MiB limit")

    if not hasattr(os, "O_NOFOLLOW"):
        raise ValidationError("this platform lacks the required no-follow file contract")
    flags = os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK
    try:
        descriptor = os.open(path, flags)
    except OSError as exc:
        raise ValidationError(f"cannot open input file without following links: {exc.strerror or exc}") from exc
    try:
        after = os.fstat(descriptor)
        if not stat.S_ISREG(after.st_mode):
            raise ValidationError("input file must be a regular file")
        if after.st_size > MAX_INPUT_BYTES:
            raise ValidationError("input file exceeds 1 MiB limit")
        if (before.st_dev, before.st_ino) != (after.st_dev, after.st_ino):
            raise ValidationError("input changed while opening")
        chunks = []
        remaining = after.st_size
        while remaining:
            chunk = os.read(descriptor, min(remaining, 65536))
            if not chunk:
                raise ValidationError("input changed while reading")
            chunks.append(chunk)
            remaining -= len(chunk)
        final = os.fstat(descriptor)
        if (after.st_size, after.st_mtime_ns, after.st_ctime_ns) != (final.st_size, final.st_mtime_ns, final.st_ctime_ns):
            raise ValidationError("input changed while reading")
        raw_contents = b"".join(chunks)
    finally:
        if descriptor != -1:
            os.close(descriptor)
    try:
        contents = raw_contents.decode("utf-8")
        loaded = json.loads(
            contents,
            parse_float=_parse_decimal_token,
            parse_int=_parse_integer_token,
            parse_constant=_reject_nonfinite,
            object_pairs_hook=_reject_duplicate_keys,
        )
    except (ValueError, UnicodeDecodeError, RecursionError) as exc:
        raise ValidationError(f"invalid JSON: {exc}") from exc
    if not isinstance(loaded, dict):
        raise ValidationError("input root must be a JSON object")
    return loaded


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Calculate offline paid-ads metrics from supplied JSON.")
    parser.add_argument("--file", required=True, help="Path to one supplied JSON observation file")
    args = parser.parse_args(argv)
    try:
        output = calculate(_read_json_file(args.file))
    except (ValidationError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(output, ensure_ascii=True, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
