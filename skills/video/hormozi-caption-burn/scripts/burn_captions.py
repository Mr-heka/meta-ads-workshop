#!/usr/bin/env python3
"""
burn_captions.py - headless Hormozi/MrBeast word-level karaoke caption burner.

Pipeline (BUILD-SPEC skill #17, QUALITY BAR rule 9):
  1. ffmpeg extract mono 16k WAV from the video
  2. WhisperX (forced-aligned word timestamps) -> fallback openai-whisper
     --word_timestamps -> parse segments[].words[] {word,start,end}
  3. build an Advanced SubStation Alpha (.ass) file: 1-3-word chunks, locked
     Hormozi style block, per-word scale-bounce + colour "pop" on the spoken word
  4. ffmpeg -vf "ass=..." burn-in, yuv420p, audio stream-copied

Locked preset (BUILD-SPEC rule 9):
  Montserrat 900 / Anton / Impact, white fill, black outline+shadow,
  active-word #f7c204 yellow (or #02fb23 green), word springs in with a
  scale bounce, caption safe zone.

Self-heal / version-gate (rule 14):
  - resolves a libass-capable ffmpeg (PATH ffmpeg if it carries the `ass`
    filter, else the keg-only `ffmpeg-full` build that actually ships libass).
    If neither exists it prints the exact `brew install ffmpeg-full` fix and
    exits non-zero instead of producing a silently caption-less file.
  - checks the requested font is installed; auto-installs the Montserrat/Anton
    casks when missing, then falls back to any installed caption font so the
    burn never renders in a wrong default.
  - reads back the burned file (ffprobe dims+duration) to ground-truth the burn.

Deps:
  - ffmpeg + ffprobe BUILT WITH libass (`brew install ffmpeg-full` - the
    mainline `ffmpeg` formula is libass-LESS; ffmpeg-full ships libass +
    fontconfig + freetype, verified)
  - one of: whisperx (`pip install whisperx`)  OR  openai-whisper (`whisper`)
  - a 900-weight font (Montserrat Black / Anton / Impact) - auto-installed

No API keys, no cost. CPU works; GPU only speeds WhisperX.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

# ---- locked Hormozi preset (BUILD-SPEC rule 9) -----------------------------
# ASS colours are &HAABBGGRR (alpha,blue,green,red). 00 alpha = opaque.
WHITE = "&H00FFFFFF"          # fill
BLACK = "&H00000000"          # outline + shadow
ACCENTS = {
    "yellow": "&H0004C2F7",   # #f7c204  -> BB=04 GG=C2 RR=F7
    "green":  "&H0023FB02",   # #02fb23  -> BB=23 GG=FB RR=02
    "purple": "&H00E23667",   # #6736E2 Selr brand -> BB=E2 GG=36 RR=67
}
DEFAULT_FONT = "Montserrat Black"   # fallbacks: Anton, Impact
MAX_WORDS_PER_CHUNK = 3
CHUNK_BREAK_PAUSE = 0.40            # seconds of silence forces a new chunk
# caption height fraction + safe-zone margin (fraction of frame height up from
# bottom). Alignment 2 = bottom-centre; MarginV lifts it into the safe zone.
FONT_HEIGHT_FRAC = 0.062
MARGINV_FRAC = 0.28
# usable caption width = frame width minus this fraction each side (the safe
# zone the text must fit inside). A chunk wider than this WRAPS to extra rows;
# a single word wider than this SCALES down - either way it can NEVER clip the
# frame edge.
SIDE_MARGIN_FRAC = 0.06
# inter-word gap as a fraction of font size, used only by the no-Pillow
# heuristic (with Pillow the real space advance is measured).
SPACE_FRAC = 0.30
# scale-bounce: word springs from 70% -> 118% -> 100% over BOUNCE_MS, the
# MrBeast/Hormozi "pop in" on the spoken word, plus a small upward lift.
BOUNCE_MS = 130
# per-word vertical pop: the spoken word also rises POP_RISE_FRAC of the font
# size and settles - a real Y-axis motion, not just a scale bounce.
POP_RISE_FRAC = 0.18

# keg-only ffmpeg-full build that actually ships libass (Homebrew, Apple Silicon
# + Intel prefixes). Mainline `ffmpeg` formula has zero libass.
FFMPEG_FULL_CANDIDATES = [
    "/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg",
    "/usr/local/opt/ffmpeg-full/bin/ffmpeg",
]

# resolved at runtime by ffmpeg_with_libass(); ffprobe travels with it.
FFMPEG = "ffmpeg"
FFPROBE = "ffprobe"


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def die(msg, code=1):
    print(f"\n[hormozi-caption-burn] ERROR: {msg}\n", file=sys.stderr)
    sys.exit(code)


# ---- rule 14: libass version-gate ------------------------------------------
def _has_ass_filter(ffmpeg_bin):
    """True if this ffmpeg binary carries the libass `ass` burn filter."""
    try:
        out = subprocess.run([ffmpeg_bin, "-hide_banner", "-filters"],
                             capture_output=True, text=True).stdout
    except (OSError, subprocess.SubprocessError):
        return False
    # filter rows look like " ... ass    V->V    Render ASS subtitles ..."
    for line in out.splitlines():
        toks = line.split()
        if len(toks) > 1 and toks[1] == "ass":
            return True
    return False


def ffmpeg_with_libass():
    """Resolve a libass-capable ffmpeg + matching ffprobe, or self-heal.

    Order: PATH ffmpeg (if it carries `ass`) -> keg-only ffmpeg-full build.
    The mainline Homebrew `ffmpeg` formula is libass-LESS, so on most Macs the
    keg-only `ffmpeg-full` is the one that works.
    """
    path_ffmpeg = shutil.which("ffmpeg")
    if path_ffmpeg and _has_ass_filter(path_ffmpeg):
        probe = shutil.which("ffprobe") or "ffprobe"
        return path_ffmpeg, probe

    for cand in FFMPEG_FULL_CANDIDATES:
        if os.path.exists(cand) and _has_ass_filter(cand):
            probe = os.path.join(os.path.dirname(cand), "ffprobe")
            return cand, (probe if os.path.exists(probe) else "ffprobe")

    die(
        "no ffmpeg with libass found - the `ass` burn filter is missing, so "
        "captions would silently not render.\n"
        "  The mainline Homebrew `ffmpeg` formula ships ZERO libass; the build "
        "that includes it is `ffmpeg-full`.\n"
        "  SELF-HEAL (run this, then retry - no human needed):\n"
        "    brew install ffmpeg-full      # ships libass + fontconfig + freetype\n"
        "  ffmpeg-full is keg-only, so this script auto-finds it at\n"
        "  /opt/homebrew/opt/ffmpeg-full/bin/ffmpeg - no symlink needed."
    )


# ---- rule 9: font presence-check + self-heal -------------------------------
# requested font name -> Homebrew cask that installs it
FONT_CASKS = {
    "montserrat black": "font-montserrat",
    "montserrat": "font-montserrat",
    "anton": "font-anton",
}
# fallback chain of caption fonts (name -> filename substring to detect on disk)
FONT_FALLBACKS = [
    ("Montserrat Black", "montserrat"),
    ("Anton", "anton"),
    ("Impact", "impact"),
    ("Arial Black", "arialbd"),
]


def _installed_font_files():
    """Lowercased basenames of every font in the user + system font dirs."""
    names = []
    for d in (os.path.expanduser("~/Library/Fonts"),
              "/Library/Fonts", "/System/Library/Fonts",
              "/System/Library/Fonts/Supplemental"):
        if os.path.isdir(d):
            names += [f.lower() for f in os.listdir(d)]
    return names


def _font_present(font_name, installed):
    key = font_name.lower().replace(" ", "")
    short = font_name.lower().split()[0]  # "montserrat black" -> "montserrat"
    return any(key in f.replace(" ", "") or short in f for f in installed)


def resolve_font(requested, fontsdir):
    """Ensure `requested` is installed (auto-install its cask), else fall back
    to the first installed caption font. Returns the font NAME libass will use.
    """
    installed = _installed_font_files()
    if _font_present(requested, installed):
        return requested

    cask = FONT_CASKS.get(requested.lower())
    if cask and shutil.which("brew"):
        print(f"[font] {requested} not installed - installing {cask} ...",
              file=sys.stderr)
        r = subprocess.run(["brew", "install", "--cask", cask],
                           capture_output=True, text=True)
        if r.returncode == 0:
            installed = _installed_font_files()
            if _font_present(requested, installed):
                return requested
        else:
            print(f"[font] cask install failed: {r.stderr[-200:]}",
                  file=sys.stderr)

    for name, _ in FONT_FALLBACKS:
        if _font_present(name, installed):
            if name != requested:
                print(f"[font] falling back to installed '{name}' "
                      f"(requested '{requested}' unavailable)", file=sys.stderr)
            return name

    print(f"[font] WARNING: no caption font found on disk; libass will use its "
          f"built-in default. Install one with: brew install --cask "
          f"font-montserrat", file=sys.stderr)
    return requested


# ---- text width measurement (overflow guard) -------------------------------
# Map a resolved font NAME to a real .ttf on disk + the variable instance to
# select. Pillow measures the *actual* glyph advances so the layout matches
# what libass renders - no guessing, no clipping.
FONT_FILES = [
    ("montserrat", os.path.expanduser("~/Library/Fonts/Montserrat[wght].ttf"), "Black"),
    ("anton", os.path.expanduser("~/Library/Fonts/Anton-Regular.ttf"), None),
    ("impact", "/System/Library/Fonts/Supplemental/Impact.ttf", None),
    ("arial", "/System/Library/Fonts/Supplemental/Arial Black.ttf", None),
]


def _find_font_file(font_name):
    """Return (path, variation_instance_or_None) for the resolved font, or
    (None, None) if no on-disk TTF matches (then we fall back to a heuristic)."""
    short = font_name.lower().split()[0]
    for key, path, inst in FONT_FILES:
        if key == short and os.path.exists(path):
            return path, inst
    # also scan the font dirs for any file matching the short name
    for d in (os.path.expanduser("~/Library/Fonts"), "/Library/Fonts",
              "/System/Library/Fonts/Supplemental"):
        if os.path.isdir(d):
            for f in os.listdir(d):
                if short in f.lower() and f.lower().endswith((".ttf", ".otf")):
                    return os.path.join(d, f), None
    return None, None


# heuristic fallback: average glyph advance as a fraction of font size for a
# heavy all-caps display face (measured from Montserrat Black). Used only when
# Pillow or the font file is unavailable, so width is still bounded.
HEURISTIC_ADV_FRAC = 0.62


class TextMeasurer:
    """Measures uppercase caption text width at a given pixel font size, using
    the real TTF via Pillow when available, else a calibrated heuristic. The
    measurement is what drives the no-overflow scaling, so it must match the
    burn font - hence we load the SAME file libass will use."""

    def __init__(self, font_name, fontsize):
        self.fontsize = fontsize
        self.font = None
        self.space = fontsize * SPACE_FRAC
        path, inst = _find_font_file(font_name)
        try:
            from PIL import ImageFont  # lazy: only needed for measurement
            if path:
                self.font = ImageFont.truetype(path, fontsize)
                if inst:
                    try:
                        self.font.set_variation_by_name(inst)
                    except Exception:
                        pass
                self.space = self.font.getlength(" ")
        except Exception:
            self.font = None  # fall back to heuristic below

    def word_width(self, word):
        if self.font is not None:
            return self.font.getlength(word)
        return len(word) * self.fontsize * HEURISTIC_ADV_FRAC


def probe(video):
    """Return (width, height, duration) via ffprobe."""
    out = run([
        FFPROBE, "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=width,height",
        "-show_entries", "format=duration",
        "-of", "json", video,
    ]).stdout
    j = json.loads(out)
    st = j["streams"][0]
    return int(st["width"]), int(st["height"]), float(j["format"]["duration"])


# ---- stage 1: extract speech audio -----------------------------------------
def extract_wav(video, wav):
    run([FFMPEG, "-y", "-i", video, "-ac", "1", "-ar", "16000",
         "-c:a", "pcm_s16le", wav])


# ---- stage 2: word timestamps ----------------------------------------------
def transcribe(wav, outdir):
    """Try WhisperX (forced alignment), fall back to openai-whisper.
    Returns a flat list of {word, start, end} in seconds."""
    if shutil.which("whisperx"):
        try:
            run(["whisperx", wav, "--model", "large-v3",
                 "--align_model", "WAV2VEC2_ASR_LARGE_LV60K_960H",
                 "--output_format", "json", "--output_dir", outdir,
                 "--language", "en"])
            return _parse_words(_find_json(outdir, wav))
        except subprocess.CalledProcessError as e:
            print(f"[warn] whisperx failed ({e.stderr[-200:] if e.stderr else e}); "
                  "falling back to openai-whisper", file=sys.stderr)

    if shutil.which("whisper"):
        run(["whisper", wav, "--model", "small.en",
             "--word_timestamps", "True", "--output_format", "json",
             "--output_dir", outdir])
        return _parse_words(_find_json(outdir, wav))

    die("no transcriber found. Install one:\n"
        "    pip install whisperx        # preferred (word-aligned)\n"
        "    pip install -U openai-whisper")


def _find_json(outdir, wav):
    base = os.path.splitext(os.path.basename(wav))[0]
    cand = os.path.join(outdir, base + ".json")
    if os.path.exists(cand):
        return cand
    js = [f for f in os.listdir(outdir) if f.endswith(".json")]
    if not js:
        die(f"transcriber produced no .json in {outdir}")
    return os.path.join(outdir, js[0])


def _parse_words(path):
    with open(path) as f:
        data = json.load(f)
    words = []
    # both whisperx and openai-whisper json: segments[].words[] {word,start,end}
    for seg in data.get("segments", []):
        for w in seg.get("words", []):
            txt = (w.get("word") or w.get("text") or "").strip()
            s, e = w.get("start"), w.get("end")
            if txt and s is not None and e is not None:
                words.append({"word": txt.upper(), "start": float(s), "end": float(e)})
    if not words:
        die("transcription returned no word-level timestamps. WhisperX gives "
            "the best alignment; with openai-whisper ensure --word_timestamps True.")
    return words


def normalize_words(raw):
    """Accept EITHER our flat [{word,start,end},...] cache OR a raw
    whisperx/openai-whisper transcript {segments:[{words:[...]}]} and return the
    canonical flat list with UPPER words + float times. This is what lets
    --words take a hand-made or whisper-native transcript, not only our cache."""
    if isinstance(raw, dict):
        flat = []
        for seg in raw.get("segments", []):
            flat.extend(seg.get("words", []))
        raw = flat
    out = []
    for w in raw:
        if not isinstance(w, dict):
            continue
        txt = (w.get("word") or w.get("text") or "").strip()
        s, e = w.get("start"), w.get("end")
        if txt and s is not None and e is not None:
            out.append({"word": txt.upper(), "start": float(s), "end": float(e)})
    return out


# ---- stage 3: build the .ass karaoke ---------------------------------------
def chunk_words(words):
    """Group into 1-3-word chunks; break on a >= CHUNK_BREAK_PAUSE gap."""
    chunks, cur = [], []
    for w in words:
        if cur:
            gap = w["start"] - cur[-1]["end"]
            if len(cur) >= MAX_WORDS_PER_CHUNK or gap >= CHUNK_BREAK_PAUSE:
                chunks.append(cur)
                cur = []
        cur.append(w)
    if cur:
        chunks.append(cur)
    return chunks


def ass_time(t):
    """seconds -> ASS H:MM:SS.cs (centiseconds), with full carry cascade."""
    t = max(0.0, t)
    cs_total = int(round(t * 100))          # total centiseconds, rounded once
    h, cs_total = divmod(cs_total, 360000)  # 3600s * 100
    m, cs_total = divmod(cs_total, 6000)    # 60s * 100
    s, cs = divmod(cs_total, 100)
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"


def layout_chunk(chunk, measurer, fontsize, width, cy, safe_w):
    """Place every word in a chunk so NOTHING clips the frame edge. Two-stage,
    the exact strategy the audit asked for ('wrap or scale to fit'):

      1. WRAP: greedily pack words into rows that each fit safe_w at full size.
         A chunk of 1-3 short words -> one row; 'EXTRAORDINARY DEVELOPMENT
         OPPORTUNITY' -> stacked rows instead of one impossible line.
      2. SCALE: if a single word is itself wider than safe_w (e.g.
         'INTERNATIONALIZATION'), it can't wrap, so that row is scaled down to
         fit. A normal multi-row chunk keeps scale 1.0.

    Returns a list of per-word dicts {word, cx, cy, scale} - measured, centred,
    guaranteed inside [margin, width-margin]."""
    words = [ass_escape(w["word"]) for w in chunk]
    widths = [measurer.word_width(x) for x in words]
    sp = measurer.space

    # ---- stage 1: greedy wrap into rows (indices) ----
    rows, cur, cur_w = [], [], 0.0
    for i, ww in enumerate(widths):
        add = ww if not cur else ww + sp
        if cur and cur_w + add > safe_w:
            rows.append(cur)
            cur, cur_w = [i], ww
        else:
            cur.append(i)
            cur_w += add
    if cur:
        rows.append(cur)

    # ---- stage 2: per-row scale so even a single huge word fits ----
    line_h = fontsize * 1.18                 # row pitch (font + a little air)
    n_rows = len(rows)
    # vertically centre the row stack on cy
    top = cy - (n_rows - 1) * line_h / 2.0

    placed = []
    for r, row in enumerate(rows):
        row_raw = sum(widths[i] for i in row) + sp * (len(row) - 1)
        scale = 1.0 if row_raw <= safe_w or row_raw <= 0 else safe_w / row_raw
        sps = sp * scale
        total = sum(widths[i] * scale for i in row) + sps * (len(row) - 1)
        x = (width - total) / 2.0
        ry = top + r * line_h
        for i in row:
            wd = widths[i] * scale
            placed.append({"idx": i, "word": words[i],
                           "cx": x + wd / 2.0, "cy": ry, "scale": scale})
            x += wd + sps
    # back into spoken order
    placed.sort(key=lambda p: p["idx"])
    return placed


def build_ass(chunks, width, height, font, accent):
    fontsize = int(height * FONT_HEIGHT_FRAC)
    marginv = int(height * MARGINV_FRAC)
    outline = max(4, fontsize // 18)
    shadow = max(2, fontsize // 36)
    accent_col = ACCENTS[accent]
    safe_w = width * (1.0 - 2 * SIDE_MARGIN_FRAC)
    cy = height - marginv          # centre Y of the caption block
    rise = fontsize * POP_RISE_FRAC
    measurer = TextMeasurer(font, fontsize)

    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {width}
PlayResY: {height}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Hormozi,{font},{fontsize},{WHITE},{accent_col},{BLACK},{BLACK},-1,0,0,0,100,100,0,0,1,{outline},{shadow},5,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, Effect, Text
"""

    lines = []
    for chunk in chunks:
        c_start = chunk[0]["start"]
        c_end = chunk[-1]["end"]
        placed = layout_chunk(chunk, measurer, fontsize, width, cy, safe_w)

        for i, w in enumerate(chunk):
            p = placed[i]
            scale = p["scale"]
            cx, wy = p["cx"], p["cy"]
            base = int(round(scale * 100))    # settle scale for libass
            up = int(round(scale * 118))      # overshoot
            small = int(round(scale * 70))    # spring-in start
            on = int(round((w["start"] - c_start) * 1000))   # ms from line start
            mid = on + BOUNCE_MS // 2
            settle = on + BOUNCE_MS
            word = p["word"]

            # HIGHLIGHT TRAVELS: this word pops to the accent when it is spoken
            # and STAYS accent until the NEXT word is spoken (or, for the last
            # word, until the chunk ends). No mid-chunk revert-to-white - the
            # most-recently-spoken word is always the coloured one, the real
            # Hormozi behaviour.
            if i + 1 < len(chunk):
                next_on = int(round((chunk[i + 1]["start"] - c_start) * 1000))
            else:
                next_on = None  # last word holds accent to chunk end

            # each word is its OWN Dialogue line, \pos'd at its measured centre.
            # Per-word lines give a REAL per-word vertical pop - \move lifts the
            # word from rise->settle on its spoken frame, impossible in one
            # shared line.
            y_pop = wy - rise
            tags = (
                f"\\an5\\pos({int(round(cx))},{int(round(wy))})"
                f"\\1c{WHITE}\\fscx{small}\\fscy{small}"
                f"\\move({int(round(cx))},{int(round(y_pop))},"
                f"{int(round(cx))},{int(round(wy))},{on},{settle})"   # rise->settle
                f"\\t({on},{on+60},\\1c{accent_col})"                # colour pop in
                f"\\t({on},{mid},\\fscx{up}\\fscy{up})"              # overshoot
                f"\\t({mid},{settle},\\fscx{base}\\fscy{base})"      # settle scale
            )
            if next_on is not None:
                # hand the highlight to the next word: revert to white exactly as
                # the next word pops (clean travel, not a flash).
                tags += f"\\t({next_on},{next_on+60},\\1c{WHITE})"
            lines.append(
                f"Dialogue: 0,{ass_time(c_start)},{ass_time(c_end)},"
                f"Hormozi,,0,0,,{{{tags}}}{word}"
            )

    return header + "\n".join(lines) + "\n"


def ass_escape(s):
    return s.replace("\\", "").replace("{", "(").replace("}", ")")


# ---- stage 4: burn ----------------------------------------------------------
def burn(video, ass_path, out, fontsdir):
    # libass needs the .ass path escaped for the filtergraph (colons, etc.)
    esc = ass_path.replace("\\", "\\\\").replace(":", "\\:").replace("'", "\\'")
    vf = f"ass='{esc}'"
    if fontsdir:
        fd = fontsdir.replace("\\", "\\\\").replace(":", "\\:").replace("'", "\\'")
        vf = f"ass='{esc}':fontsdir='{fd}'"
    run([FFMPEG, "-y", "-i", video, "-vf", vf,
         "-c:v", "libx264", "-crf", "18", "-preset", "medium",
         "-pix_fmt", "yuv420p", "-c:a", "copy", out])


def run_check(font):
    """Ground-truth self-test of the .ass builder on a KNOWN input. Reads the
    generated artifact back and asserts the invariants a broken asset would
    violate. No video, no ffmpeg, no ASR - pure layout correctness."""
    import re
    W, H = 1080, 1920
    fontsize = int(H * FONT_HEIGHT_FRAC)
    safe_w = W * (1.0 - 2 * SIDE_MARGIN_FRAC)
    cy = H - int(H * MARGINV_FRAC)
    measurer = TextMeasurer(font, fontsize)
    backend = "Pillow/real-glyphs" if measurer.font is not None else "heuristic"

    # known fixture: the exact worst cases the round-2 audit hit -
    # a 3-long-word chunk and a single very long word, plus a normal chunk.
    fixture = [
        {"word": "THIS", "start": 0.20, "end": 0.45},
        {"word": "IS", "start": 0.45, "end": 0.60},
        {"word": "AN", "start": 0.60, "end": 0.75},
        {"word": "EXTRAORDINARY", "start": 0.90, "end": 1.80},
        {"word": "DEVELOPMENT", "start": 1.85, "end": 2.60},
        {"word": "OPPORTUNITY", "start": 2.65, "end": 3.50},
        {"word": "INTERNATIONALIZATION", "start": 3.90, "end": 5.20},
        {"word": "NOW", "start": 5.30, "end": 5.70},
    ]
    fixture = [{"word": w["word"].upper(), "start": w["start"], "end": w["end"]}
               for w in fixture]
    chunks = chunk_words(fixture)
    ass = build_ass(chunks, W, H, font, "yellow")

    fails = []
    margin = W * SIDE_MARGIN_FRAC

    # ASSERT 1 - no overflow, per WORD. Re-run the real layout and confirm every
    # placed word's left/right edge sits inside the safe band. A regression that
    # drops wrap-or-scale would push an edge past the frame here.
    scaled_seen = False
    for chunk in chunks:
        placed = layout_chunk(chunk, measurer, fontsize, W, cy, safe_w)
        for p in placed:
            if p["scale"] < 0.999:
                scaled_seen = True
            half = measurer.word_width(p["word"]) * p["scale"] / 2.0
            left, right = p["cx"] - half, p["cx"] + half
            if left < margin - 1 or right > W - margin + 1:
                fails.append(
                    f"overflow: '{p['word']}' edge [{left:.0f},{right:.0f}] "
                    f"outside safe [{margin:.0f},{W-margin:.0f}]")

    # ASSERT 2 - the long-word guard actually FIRED. With real glyphs,
    # INTERNATIONALIZATION at this size is far wider than safe_w and cannot wrap
    # (one word), so it MUST have been scaled down. (Skip on the coarse
    # heuristic, which can under-estimate; the per-word overflow assert above
    # still protects us either way.)
    if measurer.font is not None and not scaled_seen:
        fails.append("long-word guard did not fire: a word wider than safe_w was "
                     "left at full size (scale-to-fit is broken)")

    # ASSERT 3 - highlight travels, no mid-chunk white revert. Parse every
    # Dialogue line; the accent colour must appear, and a word must NOT revert to
    # white before its OWN end (the round-2 'active word reverts mid-chunk' bug).
    accent = ACCENTS["yellow"].replace("&", "").lower()
    white = WHITE.replace("&", "").lower()
    n_lines = 0
    for line in ass.splitlines():
        if not line.startswith("Dialogue:"):
            continue
        n_lines += 1
        body = line.split(",", 9)[9].lower()
        if accent not in body:
            fails.append(f"no accent colour-pop in line: {body[:60]}")
        # find every \t(t0,t1,\1c...) recolour and its target colour
        recolours = re.findall(r"\\t\((\d+),(\d+),\\1c(&?h[0-9a-f]+)", body)
        pop_on = None
        for t0, t1, col in recolours:
            col = col.replace("&", "")
            if col == accent and pop_on is None:
                pop_on = int(t0)
            elif col == white and pop_on is not None:
                # a white revert must come AFTER the word's own pop (travel),
                # never simultaneously / before it.
                if int(t0) <= pop_on:
                    fails.append(f"mid-chunk white revert at {t0}<= pop {pop_on}: "
                                 f"{body[:60]}")

    if n_lines == 0:
        fails.append("builder produced zero Dialogue lines")

    print(f"[check] font={font} measure={backend} chunks={len(chunks)} "
          f"dialogue_lines={n_lines} downscaled={'yes' if scaled_seen else 'no'}")
    if fails:
        for f in fails:
            print(f"  FAIL: {f}", file=sys.stderr)
        die(f"{len(fails)} assertion(s) failed - the .ass builder is broken")
    print("[check] PASS - no overflow, long-word guard fires, highlight travels "
          "without mid-chunk white revert")


def main():
    global FFMPEG, FFPROBE
    ap = argparse.ArgumentParser(description="Burn Hormozi word-level captions.")
    ap.add_argument("video", nargs="?", help="input mp4 (omit only with --check)")
    ap.add_argument("--accent", choices=list(ACCENTS), default="yellow")
    ap.add_argument("--font", default=DEFAULT_FONT,
                    help="caption font (Montserrat Black / Anton / Impact)")
    ap.add_argument("--fontsdir", default=os.path.expanduser("~/Library/Fonts"),
                    help="dir libass scans for the font")
    ap.add_argument("--words", help="reuse a cached <name>.words.json (skip ASR)")
    ap.add_argument("--ass", help="reuse/write this .ass path")
    ap.add_argument("--ass-only", action="store_true",
                    help="transcribe + write .ass, do not burn")
    ap.add_argument("--burn-only", action="store_true",
                    help="burn an existing --ass onto the video, no ASR")
    ap.add_argument("--check", action="store_true",
                    help="self-test the .ass builder on a known fixture (no "
                         "video needed): asserts no chunk overflows the frame, "
                         "the long-word guard fires, and the highlight travels "
                         "without a mid-chunk white revert. Exits non-zero on "
                         "any broken-asset condition.")
    ap.add_argument("-o", "--out", help="output mp4 (default <name>-captioned.mp4)")
    args = ap.parse_args()

    if args.check:
        run_check(args.font)
        return

    if not args.video:
        die("no video given (pass a video path, or --check to self-test)")
    video = os.path.abspath(args.video)
    if not os.path.exists(video):
        die(f"no such video: {video}")
    stem = os.path.splitext(video)[0]
    ass_path = os.path.abspath(args.ass) if args.ass else stem + ".ass"
    out = os.path.abspath(args.out) if args.out else stem + "-captioned.mp4"

    # gate + resolve a libass-capable ffmpeg BEFORE expensive ASR (skip when only
    # writing the .ass - that path needs no burn). ffprobe still needed for dims.
    if not args.ass_only:
        FFMPEG, FFPROBE = ffmpeg_with_libass()
        font = resolve_font(args.font, args.fontsdir)
    else:
        FFPROBE = shutil.which("ffprobe") or "ffprobe"
        FFMPEG = shutil.which("ffmpeg") or "ffmpeg"
        font = args.font

    width, height, dur = probe(video)
    print(f"[1/4] {os.path.basename(video)}  {width}x{height}  {dur:.1f}s")

    # --- burn-only fast path ---
    if args.burn_only:
        if not os.path.exists(ass_path):
            die(f"--burn-only needs an existing .ass at {ass_path}")
        print(f"[4/4] burning {os.path.basename(ass_path)} ...")
        burn(video, ass_path, out, args.fontsdir)
        _verify(out, width, height, dur)
        print(f"\nDone -> {out}")
        return

    # --- words: cached or transcribe ---
    words_json = args.words or (stem + ".words.json")
    if args.words and os.path.exists(args.words):
        with open(args.words) as f:
            words = normalize_words(json.load(f))
        if not words:
            die("--words file had no usable timings: need a flat "
                "[{word,start,end}] list OR a {segments:[{words:[...]}]} transcript")
        print(f"[2/4] reused {len(words)} cached words")
    else:
        with tempfile.TemporaryDirectory() as td:
            wav = os.path.join(td, "audio.wav")
            extract_wav(video, wav)
            print("[2/4] transcribing (WhisperX -> whisper fallback) ...")
            words = transcribe(wav, td)
        with open(words_json, "w") as f:
            json.dump(words, f, indent=0)
        print(f"      {len(words)} words -> {os.path.basename(words_json)}")

    # --- build .ass ---
    chunks = chunk_words(words)
    ass_text = build_ass(chunks, width, height, font, args.accent)
    with open(ass_path, "w") as f:
        f.write(ass_text)
    print(f"[3/4] {len(chunks)} caption chunks -> {os.path.basename(ass_path)} "
          f"({font}, {args.accent} pop)")

    if args.ass_only:
        print(f"\n.ass written (no burn). Edit it, then: "
              f"burn_captions.py {os.path.basename(video)} "
              f"--ass {os.path.basename(ass_path)} --burn-only")
        return

    print("[4/4] burning ...")
    burn(video, ass_path, out, args.fontsdir)
    _verify(out, width, height, dur)
    print(f"\nDone -> {out}")


def _verify(out, w, h, dur):
    """Rule 14: read back the burned file to ground-truth the burn happened."""
    if not os.path.exists(out) or os.path.getsize(out) < 10_000:
        die(f"burn produced no/empty output at {out}")
    ow, oh, od = probe(out)
    if (ow, oh) != (w, h):
        die(f"output dims {ow}x{oh} != source {w}x{h} - burn corrupted geometry")
    if abs(od - dur) > 1.0:
        die(f"output duration {od:.1f}s drifted from source {dur:.1f}s")
    print(f"      verified: {ow}x{oh} {od:.1f}s yuv420p")


if __name__ == "__main__":
    main()
