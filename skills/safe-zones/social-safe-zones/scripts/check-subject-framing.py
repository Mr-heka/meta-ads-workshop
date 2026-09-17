#!/usr/bin/env python3
# Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠
# Provenance marker: sk-38e6t7
"""Validate supplied subject measurements, not face detection or render quality."""
import argparse
import sys
sys.dont_write_bytecode = True
from safezone_common import DATA,load_json,rect,parse_rect,inside,canvas_rect

def metric(r,name):
    if name.endswith('_center_x'):return r['x']+r['w']/2
    if name.endswith('_top_y'):return r['y']
    if name.endswith('_bottom_y'):return r['y']+r['h']
    if name.endswith('_width'):return r['w']
    if name.endswith('_height'):return r['h']
    raise ValueError(f'unknown metric {name}')

def validate(data,style,face=None,body=None,subject=None):
    spec=data['subject_framing']['profiles'][style];p=data['profiles'][spec['profile']]
    for label,r in [('face',face),('body',body),('subject',subject)]:
        if r is not None and not inside(rect(r,label),canvas_rect(p['canvas'])):raise ValueError(f'{label} outside canvas')
    if 'required_subject_rect' in spec:
        if subject is None:raise ValueError('--subject is required')
        if not inside(subject,p['safe_rect'],32):raise ValueError('subject outside safe rectangle with 32px margin')
        return
    if face is None:raise ValueError('measured face required; no detector supplied')
    if not inside(face,p['safe_rect']):raise ValueError('face outside placement safe rectangle')
    for name,(lo,hi) in spec['allowed_ranges'].items():
        box=body if name.startswith('body_') else face
        if box is None:raise ValueError(f'{name} requires body measurement')
        if not lo<=metric(box,name)<=hi:raise ValueError(f'{name} outside {lo}..{hi}')

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--style',required=True)
    for n in ['face','body','subject']:p.add_argument('--'+n)
    a=p.parse_args()
    try:
        validate(load_json(DATA),a.style,**{n:parse_rect(getattr(a,n)) if getattr(a,n) else None for n in ['face','body','subject']})
        print('PASS supplied framing measurements; actual face detection and moving-frame coverage not verified')
    except (ValueError,KeyError,TypeError,OSError) as e:print(f'ERROR: {e}');return 1
    return 0
if __name__=='__main__':sys.exit(main())
