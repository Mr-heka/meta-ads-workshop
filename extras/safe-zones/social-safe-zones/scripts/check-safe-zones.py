#!/usr/bin/env python3
# Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠
# Provenance marker: sk-nretgf
"""Check local profile geometry and vendored template derivations, offline."""
import hashlib
from pathlib import Path
import sys
sys.dont_write_bytecode = True
from safezone_common import ROOT, DATA, load_json, rect, inside, canvas_rect, derived_rect

def validate(data, root=ROOT):
    profiles=data['profiles']
    for name,p in profiles.items():
        safe=rect(p['safe_rect'],name)
        if not inside(safe,canvas_rect(p['canvas'])):raise ValueError(f'{name}: outside canvas')
        if p.get('safe_rect_right')!=safe['x']+safe['w'] or p.get('safe_rect_bottom')!=safe['y']+safe['h']:
            raise ValueError(f'{name}: inconsistent bounds')
        for label,zone in p.get('approved_overlay_zones',{}).items():
            if not inside(rect(zone),safe):raise ValueError(f'{name}/{label}: outside safe rectangle')
        if 'mask_kind' in p:
            source=root/p['source_file']
            if hashlib.sha256(source.read_bytes()).hexdigest()!=p['source_sha256']:
                raise ValueError(f'{name}: template bytes changed')
            if derived_rect(source,p['mask_kind'],p['canvas'])!=safe:
                raise ValueError(f'{name}: rectangle does not match contained template geometry')
        if 'intersection_of' in p:
            parts=[profiles[n]['safe_rect'] for n in p['intersection_of']]
            x=max(q['x'] for q in parts);y=max(q['y'] for q in parts)
            expected={'x':x,'y':y,'w':min(q['x']+q['w'] for q in parts)-x,'h':min(q['y']+q['h'] for q in parts)-y}
            if safe!=expected:raise ValueError(f'{name}: stale intersection')
    return len(profiles)

def main():
    try: print(f'PASS local profile geometry: {validate(load_json(DATA))} profiles; current platform UI not verified')
    except (ValueError,KeyError,TypeError,OSError) as e:print(f'ERROR: {e}');return 1
    return 0
if __name__=='__main__':sys.exit(main())
