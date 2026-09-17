#!/usr/bin/env python3
# Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠
# Provenance marker: sk-46rclf
"""Render authored Instagram planning overlays from canonical data.

Imports do not write. --out is explicit; existing targets require --overwrite.
These crop assumptions are Selr presets, not current Instagram certification.
"""
import argparse
import json
from pathlib import Path
import sys
sys.dont_write_bytecode = True
from PIL import Image, ImageDraw, ImageFont
from safezone_common import DATA, load_json, inside, canvas_rect

KEYS=('ig_post_4x5_1080x1350_grid_safe','ig_reel_cover_9x16_1080x1920_grid_safe')

def render(profile):
    c=profile['canvas'];s=profile['safe_rect']
    if not inside(s,canvas_rect(c)):raise ValueError('invalid safe rectangle')
    im=Image.new('RGBA',(c['w'],c['h']),(0,0,0,75));d=ImageDraw.Draw(im)
    box=(s['x'],s['y'],s['x']+s['w']-1,s['y']+s['h']-1)
    d.rectangle(box,fill=(0,0,0,0),outline=(103,54,226,255),width=4)
    try:font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',22)
    except OSError:font=ImageFont.load_default(size=22)
    d.rectangle((10,10,c['w']-11,54),fill=(20,20,20,230))
    d.text((20,20),'SELR PLANNING PRESET | verify the intended placement',font=font,fill=(255,255,255,255))
    for name,r in profile.get('crops',{}).items():
        d.rectangle((r['x'],r['y'],r['x']+r['w']-1,r['y']+r['h']-1),outline=(180,69,46,180),width=2)
    return im

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);p.add_argument('--overwrite',action='store_true');a=p.parse_args()
    try:
        profiles=load_json(DATA)['profiles'];targets=[a.out/Path(profiles[k]['overlay_file']).name for k in KEYS]
        targets.append(a.out/'profiles.json')
        if any(x.exists() or x.is_symlink() for x in targets) and not a.overwrite:raise ValueError('output exists; choose another directory or explicitly --overwrite')
        if any(x.is_symlink() for x in targets):raise ValueError('refusing symlink output')
        images=[render(profiles[k]) for k in KEYS];a.out.mkdir(parents=True,exist_ok=True)
        for image,target in zip(images,targets):image.save(target);print(target)
        targets[-1].write_text(json.dumps({k:profiles[k] for k in KEYS},indent=2)+'\n')
    except (ValueError,OSError,KeyError) as e:print(f'ERROR: {e}');return 1
    return 0
if __name__=='__main__':sys.exit(main())
