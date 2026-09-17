#!/usr/bin/env python3
# Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠
# Provenance marker: sk-1wzi6mh
"""Validate a declared placement PLAN. Never certifies rendered media or upload."""
import argparse
import importlib.util
from pathlib import Path
import sys
sys.dont_write_bytecode = True
from safezone_common import DATA,load_json,number,rect,inside,overlaps,canvas_rect

spec=importlib.util.spec_from_file_location('framing_check',Path(__file__).with_name('check-subject-framing.py'))
framing_check=importlib.util.module_from_spec(spec);spec.loader.exec_module(framing_check)

def object_field(obj,key):
    value=obj.get(key)
    if not isinstance(value,dict) or not value:raise ValueError(f'{key} requires a nonempty object')
    return value

def text_field(obj,key):
    value=obj.get(key)
    if not isinstance(value,str) or not value.strip():raise ValueError(f'{key} requires nonempty text')
    return value

def validate(m,data):
    if not isinstance(m,dict):raise ValueError('manifest must be an object')
    source=object_field(m,'source');text_field(source,'source_name');text_field(source,'mime_type')
    assessment=object_field(m,'content_assessment');text_field(assessment,'summary')
    decision=object_field(m,'route_decision');route=text_field(decision,'route');expected=data['route_decision']['routes'][route]
    text_field(decision,'reason')
    for key in ['content_style','renderer_skill']:
        if decision.get(key)!=expected[key]:raise ValueError(f'route requires {key}={expected[key]}')
    p=data['profiles'][text_field(m,'safe_zone_profile')];canvas=canvas_rect(p['canvas'])
    context=object_field(m,'placement_context');text_field(context,'evidence')
    for key,value in p.get('conditions',{}).items():
        if type(context.get(key)) is not type(value) or context.get(key)!=value:raise ValueError(f'profile condition {key} must be {value!r}')
    technical=object_field(m,'technical')
    for dim in ['width','height']:
        if number(technical.get(dim),dim,True)!=p['canvas']['w' if dim=='width' else 'h']:raise ValueError('technical canvas differs from placement profile')
    static=route=='carousel_static';duration=None
    if not static:duration=number(technical.get('duration_seconds'),'duration_seconds',True);number(technical.get('fps'),'fps',True)
    framing=m.get('subject_framing');required=expected.get('subject_framing_profile')
    if required:
        if not isinstance(framing,dict) or framing.get('profile')!=required:raise ValueError('route requires matching subject_framing')
        text_field(framing,'sample_frame_path');text_field(framing,'measurement_method')
        framing_check.validate(data,required,framing.get('face_box'),framing.get('body_box'),framing.get('subject_box'))
    # A single box covers the declared whole clip conservatively. Extra moving
    # face samples can be supplied; every overlay is checked against all boxes.
    faces=[]
    if framing and framing.get('face_box'):faces.append(framing['face_box'])
    samples=m.get('face_boxes',[])
    if not isinstance(samples,list):raise ValueError('face_boxes must be a list')
    faces+=samples
    for face in faces:
        if not inside(rect(face,'face'),p['safe_rect']):raise ValueError('face outside selected safe rectangle')
    placement=object_field(m,'placement_plan');overlays=placement.get('overlays')
    if not isinstance(overlays,list):raise ValueError('overlays must be a list (empty allowed for no overlays)')
    for overlay in overlays:
        if not isinstance(overlay,dict):raise ValueError('overlay must be an object')
        text_field(overlay,'type');r=rect(overlay.get('rect'),'overlay.rect')
        if not inside(r,p['safe_rect']):raise ValueError('overlay outside safe rectangle')
        if not static:
            start=number(overlay.get('start'),'overlay.start');end=number(overlay.get('end'),'overlay.end')
            if not 0<=start<end<=duration:raise ValueError('overlay timing outside clip')
        if any(overlaps(r,f,data['human_aware_rules']['face_padding_px']) for f in faces):raise ValueError('overlay overlaps supplied face protection area')
    build=object_field(m,'build_plan');text_field(build,'renderer_command')
    export=object_field(m,'export');ep=data['export_profiles'][text_field(export,'profile')]
    if static:
        if export['profile']!='carousel_feed_static':raise ValueError('static route requires static export profile')
        if export.get('format') not in ['png','jpg','pdf']:raise ValueError('static format must be png, jpg or pdf')
    else:
        if 'canvas' not in ep:raise ValueError('video route requires video export profile')
        if ep['canvas']!=p['canvas']:raise ValueError('export canvas differs from placement plan')
    # Legacy qc booleans and asserted codec/bitrate are not evidence. Explicitly
    # report this script's scope even if supplied values say everything passed.
    return 'static' if static else 'video'

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('manifest',type=Path);a=p.parse_args()
    try:
        kind=validate(load_json(a.manifest),load_json(DATA))
        print(f'PASS {kind} placement PLAN only; QC flags ignored; render, audio, export and publishing NOT verified')
    except (ValueError,KeyError,TypeError,OSError) as e:print(f'ERROR: {e}');return 1
    return 0
if __name__=='__main__':sys.exit(main())
