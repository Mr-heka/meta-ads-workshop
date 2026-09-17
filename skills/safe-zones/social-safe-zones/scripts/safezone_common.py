# Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠
# Provenance marker: sk-1dzp6t9
"""Local geometry and strict input helpers shared by the six offline checks."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/social-safe-zones.json'

def load_json(path):
    def invalid(value): raise ValueError(f'non-finite JSON number: {value}')
    return json.loads(Path(path).read_text(), parse_constant=invalid)

def number(value, label, positive=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f'{label} must be a finite number')
    if positive and value <= 0: raise ValueError(f'{label} must be positive')
    return value

def rect(value, label='rect'):
    if not isinstance(value, dict) or set(value) != {'x','y','w','h'}:
        raise ValueError(f'{label} requires x,y,w,h')
    for k in value: number(value[k], f'{label}.{k}', k in {'w','h'})
    return value

def parse_rect(raw):
    try: values = list(map(float, raw.split(',')))
    except (ValueError, AttributeError): raise ValueError('use finite x,y,w,h')
    if len(values) != 4: raise ValueError('use x,y,w,h')
    return rect(dict(zip(('x','y','w','h'), values)))

def inside(a, b, margin=0):
    rect(a); rect(b)
    return (a['x'] >= b['x']+margin and a['y'] >= b['y']+margin and
            a['x']+a['w'] <= b['x']+b['w']-margin and
            a['y']+a['h'] <= b['y']+b['h']-margin)

def overlaps(a,b,padding=0):
    return (a['x'] < b['x']+b['w']+padding and a['x']+a['w'] > b['x']-padding and
            a['y'] < b['y']+b['h']+padding and a['y']+a['h'] > b['y']-padding)

def canvas_rect(canvas):
    return rect({'x':0,'y':0,'w':canvas['w'],'h':canvas['h']}, 'canvas')

def box_rect(box):
    x,y,right,bottom=box
    return {'x':int(x),'y':int(y),'w':int(right-x),'h':int(bottom-y)}

def largest_rectangle(mask):
    """Largest all-true rectangle, with deterministic first maximum tie break.

    Histogram scan uses runs of identical rows to avoid rescanning large flat
    template bands. Bounds are half-open; notches and holes remain excluded.
    """
    import numpy as np
    mask=np.asarray(mask,dtype=bool)
    if mask.ndim!=2 or not mask.size: raise ValueError('empty/non-2D mask')
    heights=np.zeros(mask.shape[1],dtype=int);best=(0,0,0,0);area=0
    ends=list(np.flatnonzero(np.any(mask[1:]!=mask[:-1],axis=1))+1)+[mask.shape[0]]
    start=0
    for end in ends:
        heights=np.where(mask[start],heights+(end-start),0); stack=[]
        for x,h in enumerate([*heights,0]):
            left=x
            while stack and stack[-1][1]>h:
                pos,height=stack.pop();left=pos;candidate=int(height)*(x-pos)
                if candidate>area:area=candidate;best=(pos,end-int(height),x,end)
            if not stack or stack[-1][1]<h:stack.append((left,int(h)))
        start=end
    if not area:raise ValueError('mask has no safe pixels')
    return best

def source_mask(path, kind):
    from PIL import Image
    import numpy as np
    with Image.open(path) as im:a=np.asarray(im.convert('RGBA')).astype('int16')
    if kind=='alpha_zero':return a[:,:,3]==0
    if kind=='tiktok_standard':
        # The reviewed standard template contains a white 50%-alpha TikTok
        # watermark inside the clear area. It is artwork, not UI exclusion.
        return (a[:,:,3]==0)|((a[:,:,:3]>=250).all(2)&(a[:,:,3]<=128))
    if kind=='anchor_green':
        return ((a[:,:,0]>=60)&(a[:,:,0]<=110)&(a[:,:,1]>=200)&(a[:,:,1]<=230)&
                (a[:,:,2]>=160)&(a[:,:,2]<=190)&(a[:,:,3]>=180)&(a[:,:,3]<=230))
    raise ValueError(f'unknown mask kind {kind}')

def derived_rect(path,kind,canvas):
    mask=source_mask(path,kind);x,y,r,b=largest_rectangle(mask)
    sx=canvas['w']/mask.shape[1];sy=canvas['h']/mask.shape[0]
    return box_rect((math.ceil(x*sx),math.ceil(y*sy),math.floor(r*sx),math.floor(b*sy)))
