#!/usr/bin/env python3
# Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠
# Provenance marker: sk-ve3n85
"""Check explicit tile content against a Selr planning rectangle.

Ink is a color heuristic, not OCR. Pill boxes must come from the renderer or
manual measurement; dark photo features are never accepted as detected pills.
Exact canvas required. No face detector or live platform verification supplied.
"""
import argparse
from pathlib import Path
import sys
sys.dont_write_bytecode = True
import numpy as np
from PIL import Image, ImageDraw
from safezone_common import DATA,load_json,parse_rect,inside,canvas_rect

KEY={'post':'ig_post_4x5_1080x1350_grid_safe','reel':'ig_reel_cover_9x16_1080x1920_grid_safe'}

def bbox(mask):
    ys,xs=np.where(mask)
    if not len(xs):return None
    return {'x':int(xs.min()),'y':int(ys.min()),'w':int(xs.max()-xs.min()+1),'h':int(ys.max()-ys.min()+1)}

def purple_ink(a):
    a=a.astype(np.int16);r,g,b=a[:,:,0],a[:,:,1],a[:,:,2]
    return (b>r+30)&(b>g+50)&(r<170)&(g<120)

def check(image,profile,expect,pill=None):
    c=profile['canvas'];safe=profile['safe_rect']
    if image.size!=(c['w'],c['h']):raise ValueError(f'exact canvas required: {c["w"]}x{c["h"]}; crop/resize deliberately first')
    findings=[]
    if expect in ('ink','both'):
        rgba=np.asarray(image.convert('RGBA'))
        ink=bbox(purple_ink(rgba[:,:,:3]) & (rgba[:,:,3] > 0))
        if ink is None:raise ValueError('expected purple ink was not detected')
        findings.append(('ink heuristic',ink))
    if expect in ('pill','both'):
        if pill is None:raise ValueError('expected pill requires --pill-box from renderer or measurement')
        findings.append(('declared pill',pill))
    for label,r in findings:
        if not inside(r,canvas_rect(c)) or not inside(r,safe):raise ValueError(f'{label} outside safe rectangle: {r}')
    return findings

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('image',type=Path);p.add_argument('--profile',choices=KEY,default='post');p.add_argument('--expect',choices=['ink','pill','both'],required=True);p.add_argument('--pill-box');p.add_argument('--out',type=Path,required=True,help='new PNG file for visual inspection');p.add_argument('--overwrite',action='store_true');a=p.parse_args()
    try:
        if a.out.suffix.lower()!='.png':raise ValueError('--out must be a PNG file')
        if a.out.resolve()==a.image.resolve() or a.out.is_symlink():raise ValueError('output must not replace source or symlink')
        if a.out.exists() and not a.overwrite:raise ValueError('output exists; choose a new file or --overwrite')
        profile=load_json(DATA)['profiles'][KEY[a.profile]]
        with Image.open(a.image) as source:im=source.convert('RGBA')
        findings=check(im,profile,a.expect,parse_rect(a.pill_box) if a.pill_box else None)
        d=ImageDraw.Draw(im);s=profile['safe_rect'];d.rectangle((s['x'],s['y'],s['x']+s['w']-1,s['y']+s['h']-1),outline=(103,54,226),width=4)
        for _,r in findings:d.rectangle((r['x'],r['y'],r['x']+r['w']-1,r['y']+r['h']-1),outline=(20,140,80),width=3)
        im.save(a.out)
        print(f'PASS declared content geometry: {len(findings)} checks; inspect {a.out}; faces and live crops unverified')
    except (ValueError,OSError,KeyError) as e:print(f'ERROR: {e}');return 1
    return 0
if __name__=='__main__':sys.exit(main())
