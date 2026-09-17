#!/usr/bin/env node
// Ad Creative — character-limit checker.
//
// The whole job of this skill is producing ad copy that actually fits each
// platform's character limits. Models are unreliable at counting characters by
// eye, so this script verifies the copy instead of trusting the count written
// next to it. Run it on the bulk CSV the skill produces BEFORE delivering, so
// nothing ships over-limit.
//
//   node skills/ad-creative/scripts/check-char-limits.mjs <copy.csv>
//   node skills/ad-creative/scripts/check-char-limits.mjs --selftest
//
// CSV shape (one row per ad, same format the skill's "Bulk CSV Output" emits):
//   a `platform` column plus any element columns named by type, e.g.
//   headline_1, headline_2, description_1, primary_text, intro_text,
//   ad_text, tweet_text, path_1, display_name. Trailing _<n> is ignored, so
//   headline_1 and headline_2 are both checked against the headline limit.
//
// Limits are the human-readable source in references/platform-specs.md mirrored
// here in machine-checkable form. Over the hard max = ERROR (the platform
// truncates or rejects). Over the recommended length but within max = WARN
// (may truncate in some placements). Reports EVERY violation, never stops at
// the first one. Exit 1 if any ERROR, else 0.

import { readFileSync } from "node:fs";

// element -> { rec, max }. rec omitted means rec === max (hard limit only).
const LIMITS = {
  google_ads: {
    headline: { max: 30 },
    description: { max: 90 },
    path: { max: 15 },
    long_headline: { max: 90 },
    business_name: { max: 25 },
  },
  meta: {
    primary_text: { rec: 125, max: 2200 },
    headline: { rec: 40, max: 255 },
    description: { rec: 30, max: 255 },
    url_display_link: { max: 40 },
  },
  linkedin: {
    intro_text: { rec: 150, max: 600 },
    headline: { rec: 70, max: 200 },
    description: { rec: 100, max: 300 },
  },
  tiktok: {
    ad_text: { rec: 80, max: 100 },
    display_name: { max: 40 },
  },
  twitter: {
    tweet_text: { max: 280 },
    headline: { max: 70 },
    description: { max: 200 },
  },
};

// Accept the common ways a platform gets written in the CSV.
const PLATFORM_ALIASES = {
  google: "google_ads",
  google_ads: "google_ads",
  googleads: "google_ads",
  adwords: "google_ads",
  meta: "meta",
  facebook: "meta",
  instagram: "meta",
  fb: "meta",
  ig: "meta",
  linkedin: "linkedin",
  tiktok: "tiktok",
  twitter: "twitter",
  x: "twitter",
};

function normalizePlatform(raw) {
  const key = String(raw || "").trim().toLowerCase().replace(/[\s/-]+/g, "_");
  return PLATFORM_ALIASES[key] || null;
}

// headline_1 -> headline, primary_text_2 -> primary_text, description -> description
function columnToElement(col) {
  return String(col).trim().toLowerCase().replace(/_\d+$/, "");
}

// Count by Unicode code points so a CSV BOM or astral emoji counts as a human
// would expect. Platforms differ on emoji weight; this is the conservative
// (1-per-codepoint) count and matches what the spec reference documents.
function charLen(s) {
  return Array.from(s).length;
}

// Minimal RFC-4180 CSV parser: handles quoted fields, "" escapes, and commas
// or newlines inside quotes. No dependency.
function parseCsv(text) {
  const rows = [];
  let row = [];
  let field = "";
  let inQuotes = false;
  const s = text.replace(/^﻿/, ""); // strip BOM
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (inQuotes) {
      if (c === '"') {
        if (s[i + 1] === '"') { field += '"'; i++; }
        else inQuotes = false;
      } else field += c;
    } else if (c === '"') {
      inQuotes = true;
    } else if (c === ",") {
      row.push(field); field = "";
    } else if (c === "\n" || c === "\r") {
      if (c === "\r" && s[i + 1] === "\n") i++;
      row.push(field); field = "";
      if (row.length > 1 || row[0] !== "") rows.push(row);
      row = [];
    } else field += c;
  }
  if (field !== "" || row.length) { row.push(field); rows.push(row); }
  return rows;
}

// Returns { errors:[...], warnings:[...] } for an array of {platform, fields:{col:val}}
function checkRows(records) {
  const errors = [];
  const warnings = [];
  records.forEach((rec, idx) => {
    const rowNo = idx + 1;
    const platform = normalizePlatform(rec.platform);
    if (!platform) {
      errors.push(`row ${rowNo}: unknown platform "${rec.platform}" (expected one of: ${Object.keys(LIMITS).join(", ")})`);
      return;
    }
    const platformLimits = LIMITS[platform];
    for (const [col, value] of Object.entries(rec.fields)) {
      if (value == null || value === "") continue;
      const element = columnToElement(col);
      const limit = platformLimits[element];
      if (!limit) continue; // not a length-constrained element (e.g. an id column)
      const len = charLen(value);
      const max = limit.max;
      const rec_ = limit.rec ?? limit.max;
      if (len > max) {
        errors.push(`row ${rowNo} ${platform}.${col}: ${len} chars, over hard max ${max} (by ${len - max}) — "${value}"`);
      } else if (len > rec_) {
        warnings.push(`row ${rowNo} ${platform}.${col}: ${len} chars, over recommended ${rec_} (by ${len - rec_}) — may truncate — "${value}"`);
      }
    }
  });
  return { errors, warnings };
}

function recordsFromCsv(text) {
  const rows = parseCsv(text);
  if (rows.length < 2) return [];
  const header = rows[0].map((h) => h.trim());
  const platformCol = header.findIndex((h) => h.toLowerCase() === "platform");
  return rows.slice(1).map((cells) => {
    const fields = {};
    header.forEach((h, i) => { if (i !== platformCol) fields[h] = cells[i] ?? ""; });
    return { platform: platformCol >= 0 ? cells[platformCol] : "", fields };
  });
}

function report({ errors, warnings }) {
  console.log("Ad Creative character-limit check");
  console.log("=================================");
  for (const w of warnings) console.log(`WARN  ${w}`);
  for (const e of errors) console.log(`ERROR ${e}`);
  console.log("");
  console.log(`Errors: ${errors.length}   Warnings: ${warnings.length}`);
  if (errors.length) console.log("FAILED — trim the over-limit copy above before delivering.");
  else if (warnings.length) console.log("PASSED with warnings — review the items that may truncate.");
  else console.log("PASSED — all copy fits.");
  return errors.length ? 1 : 0;
}

function selftest() {
  const csv = [
    "platform,headline_1,headline_2,description_1,primary_text",
    // google headline_2 is 31 chars (over 30) -> ERROR; description ok
    'google_ads,"Automate Your Weekly Reports","Reports Done in 5 Min, Not 5 Hr","Save 10+ hrs/week. Start free.",',
    // meta primary_text 130 chars -> over rec 125, under max -> WARN
    `meta,"Short hook","","","${"x".repeat(130)}"`,
    // linkedin clean
    'linkedin,"A clean professional headline","","A tidy description well under the limit.",',
    // unknown platform -> ERROR
    'pinterest,"whatever","","",',
  ].join("\n");
  const records = recordsFromCsv(csv);
  const { errors, warnings } = checkRows(records);
  // Match real findings by their "platform.column" tag (e.g. "linkedin.headline_1"),
  // not a bare platform name — the unknown-platform error lists every platform
  // in its "expected one of" hint, which would otherwise false-match.
  const findings = [...errors, ...warnings];
  const checks = [
    [errors.some((e) => e.includes("google_ads.headline_2")), "google over-limit headline flagged as ERROR"],
    [warnings.some((w) => w.includes("meta.primary_text")), "meta over-recommended primary_text flagged as WARN"],
    [errors.some((e) => e.includes('unknown platform "pinterest"')), "unknown platform flagged as ERROR"],
    [!findings.some((m) => m.includes("linkedin.")), "clean linkedin row produced no findings"],
  ];
  let ok = true;
  for (const [pass, name] of checks) {
    console.log(`${pass ? "PASS" : "FAIL"}  ${name}`);
    if (!pass) ok = false;
  }
  console.log("");
  console.log(ok ? "selftest PASSED" : "selftest FAILED");
  return ok ? 0 : 1;
}

function main() {
  const arg = process.argv[2];
  if (!arg || arg === "--help" || arg === "-h") {
    console.log("Usage: node check-char-limits.mjs <copy.csv>");
    console.log("       node check-char-limits.mjs --selftest");
    process.exit(arg ? 0 : 1);
  }
  if (arg === "--selftest") process.exit(selftest());
  let text;
  try {
    text = readFileSync(arg, "utf8");
  } catch (err) {
    console.error(`Cannot read ${arg}: ${err.message}`);
    process.exit(1);
  }
  const records = recordsFromCsv(text);
  if (!records.length) {
    console.error("No data rows found. Expected a header row with a 'platform' column plus element columns.");
    process.exit(1);
  }
  process.exit(report(checkRows(records)));
}

main();
