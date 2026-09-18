#!/usr/bin/env python3
# Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠
# Provenance marker: sk-wlakri
"""Offline regression controls for all six commands and shared geometry."""
import copy
import importlib.util
import json
from pathlib import Path
import struct
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import numpy as np
from PIL import Image,ImageDraw

sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from safezone_common import DATA,ROOT,load_json,largest_rectangle,source_mask,inside

def load(name):
    spec=importlib.util.spec_from_file_location(name.replace('-','_'),HERE/(name+'.py'))
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

geometry=load('check-safe-zones');tile=load('check-tile-safe-zone');subject=load('check-subject-framing')
manifest=load('check-production-manifest');export=load('check-export-quality');generator=load('make-instagram-overlays')
D=load_json(DATA)
M=load_json(ROOT/'examples/production-manifest.example.json')
PROFILE=D['export_profiles']['phone_ready_vertical_reel_1080x1920']

def probe():
    return {'format':{'duration':'2','bit_rate':'999999999'},'streams':[
        {'codec_type':'video','codec_name':'h264','width':1080,'height':1920,'pix_fmt':'yuv420p','field_order':'progressive','sample_aspect_ratio':'1:1','color_space':'bt709','color_transfer':'bt709','color_primaries':'bt709','bit_rate':'8000000','avg_frame_rate':'25/1','r_frame_rate':'25/1'},
        {'codec_type':'audio','codec_name':'aac','sample_rate':'48000','channels':2,'bit_rate':'256000'}]}

def box(kind,payload=b''):
    return struct.pack('>I4s',8+len(payload),kind)+payload
FTYP=box(b'ftyp',b'isom'+b'\0'*4+b'iso2')

class Controls(unittest.TestCase):
    def setUp(self):self.tmp=tempfile.TemporaryDirectory(prefix='safezone-controls-');self.out=Path(self.tmp.name)
    def tearDown(self):self.tmp.cleanup()
    def run_cli(self,name,*args):
        return subprocess.run([sys.executable,'-B',str(HERE/(name+'.py')),*map(str,args)],capture_output=True,text=True,timeout=30)
    def test_profiles_rederive_actual_templates(self):self.assertEqual(geometry.validate(D),14)
    def test_notched_mask_not_bbox(self):
        mask=np.ones((10,10),bool);mask[:3,6:]=False
        r=largest_rectangle(mask);self.assertEqual(r,(0,3,10,10));self.assertTrue(mask[r[1]:r[3],r[0]:r[2]].all())
    def test_all_derived_rect_pixels_are_safe(self):
        import math
        for key,p in D['profiles'].items():
            if 'mask_kind' not in p:continue
            with self.subTest(profile=key):
                mask=source_mask(ROOT/p['source_file'],p['mask_kind']);r=p['safe_rect']
                sx=mask.shape[1]/p['canvas']['w'];sy=mask.shape[0]/p['canvas']['h']
                area=mask[math.floor(r['y']*sy):math.ceil((r['y']+r['h'])*sy),math.floor(r['x']*sx):math.ceil((r['x']+r['w'])*sx)]
                self.assertTrue(area.size);self.assertTrue(area.all())
    def test_tiktok_watermark_allowance_does_not_allow_colored_notch(self):
        key='tiktok_in_feed_standard_9x16_1080x1920'
        mask=source_mask(ROOT/D['profiles'][key]['source_file'],'tiktok_standard')
        self.assertTrue(mask[1500,1440]);self.assertFalse(mask[2500,2300]);self.assertFalse(mask[4000,1000])
    def test_changed_vendor_hash_rejected(self):
        d=copy.deepcopy(D);d['profiles']['youtube_video_ads_vertical_9x16_1080x1920']['source_sha256']='0'*64
        with self.assertRaises(ValueError):geometry.validate(d)
    def test_empty_mask_rejected(self):
        with self.assertRaises(ValueError):largest_rectangle(np.zeros((2,2),bool))
    def test_restored_unsafe_bbox_rejected(self):
        d=copy.deepcopy(D);p=d['profiles']['youtube_video_ads_square_1080x1080'];p['safe_rect']={'x':48,'y':48,'w':931,'h':642}
        with self.assertRaises(ValueError):geometry.validate(d)
    def test_bad_subzone_rejected(self):
        d=copy.deepcopy(D);d['profiles']['ig_reel_cover_9x16_1080x1920_grid_safe']['approved_overlay_zones']['face']['h']=620
        with self.assertRaises(ValueError):geometry.validate(d)
    def test_stale_intersection_rejected(self):
        d=copy.deepcopy(D);d['profiles']['universal_vertical_9x16_1080x1920']['safe_rect']['w']=768
        with self.assertRaises(ValueError):geometry.validate(d)
    def test_generator_import_does_not_write(self):
        with patch.object(Path,'mkdir',side_effect=AssertionError('mkdir')),patch.object(Image.Image,'save',side_effect=AssertionError('save')),patch.object(Path,'write_text',side_effect=AssertionError('write')):load('make-instagram-overlays')
    def test_generator_outputs_and_refuses_overwrite(self):
        first=self.run_cli('make-instagram-overlays','--out',self.out);self.assertEqual(first.returncode,0,first.stdout)
        before={p.name:p.read_bytes() for p in self.out.iterdir()}
        second=self.run_cli('make-instagram-overlays','--out',self.out);self.assertNotEqual(second.returncode,0)
        self.assertEqual(before,{p.name:p.read_bytes() for p in self.out.iterdir()})
        self.assertEqual(load_json(self.out/'profiles.json'),{k:D['profiles'][k] for k in generator.KEYS})
    def test_signed_purple_math(self):
        pixels=np.array([[[255,255,255],[10,240,250],[103,54,226]]],dtype=np.uint8)
        self.assertEqual(tile.purple_ink(pixels).tolist(),[[False,False,True]])
    def test_blank_expected_ink_fails(self):
        with self.assertRaises(ValueError):tile.check(Image.new('RGB',(1080,1350),'white'),D['profiles'][tile.KEY['post']],'ink')
    def test_fully_transparent_purple_is_not_ink(self):
        im=Image.new('RGBA',(1080,1350),(255,255,255,0))
        ImageDraw.Draw(im).rectangle((200,300,600,400),fill=(103,54,226,0))
        with self.assertRaises(ValueError):tile.check(im,D['profiles'][tile.KEY['post']],'ink')
        im.putpixel((300,350),(103,54,226,255))
        self.assertEqual(tile.check(im,D['profiles'][tile.KEY['post']],'ink')[0][1],{'x':300,'y':350,'w':1,'h':1})
    def test_dark_photo_is_not_pill(self):
        im=Image.new('RGB',(1080,1350),'white');ImageDraw.Draw(im).rectangle((200,300,900,350),fill='black')
        with self.assertRaises(ValueError):tile.check(im,D['profiles'][tile.KEY['post']],'pill')
    def test_wrong_aspect_and_dimensions_rejected(self):
        for size in [(1080,1920),(540,675)]:
            with self.subTest(size=size),self.assertRaises(ValueError):tile.check(Image.new('RGB',size,'white'),D['profiles'][tile.KEY['post']],'pill',{'x':200,'y':300,'w':300,'h':100})
    def test_last_pixel_boundary(self):
        p=D['profiles'][tile.KEY['post']]
        for x,good in [(965,True),(966,False)]:
            im=Image.new('RGB',(1080,1350),'white');im.putpixel((x,300),(103,54,226))
            if good:self.assertEqual(len(tile.check(im,p,'ink')),1)
            else:
                with self.assertRaises(ValueError):tile.check(im,p,'ink')
    def test_explicit_pill_geometry(self):
        im=Image.new('RGB',(1080,1920),'gray');p=D['profiles'][tile.KEY['reel']]
        self.assertEqual(len(tile.check(im,p,'pill',{'x':200,'y':500,'w':500,'h':150})),1)
        with self.assertRaises(ValueError):tile.check(im,p,'pill',{'x':200,'y':450,'w':500,'h':150})
    def test_tile_output_no_overwrite(self):
        source=self.out/'source.png';im=Image.new('RGB',(1080,1350),'white');ImageDraw.Draw(im).rectangle((200,300,600,400),fill=(103,54,226));im.save(source)
        target=self.out/'check.png';argv=[source,'--expect','ink','--out',target]
        self.assertEqual(self.run_cli('check-tile-safe-zone',*argv).returncode,0)
        before=target.read_bytes();self.assertNotEqual(self.run_cli('check-tile-safe-zone',*argv).returncode,0);self.assertEqual(target.read_bytes(),before)
        self.assertNotEqual(self.run_cli('check-tile-safe-zone',source,'--expect','ink','--out',source,'--overwrite').returncode,0)
    def test_subject_positive(self):subject.validate(D,'talking_head_full_1080x1920',M['subject_framing']['face_box'],M['subject_framing']['body_box'])
    def test_subject_huge_offcanvas_and_nonfinite(self):
        for face in [{'x':-1000,'y':600,'w':3080,'h':360},{'x':400,'y':600,'w':20,'h':360},{'x':float('nan'),'y':600,'w':360,'h':360}]:
            with self.subTest(face=face),self.assertRaises(ValueError):subject.validate(D,'talking_head_full_1080x1920',face,M['subject_framing']['body_box'])
    def test_subject_missing_body_and_subject_fail(self):
        with self.assertRaises(ValueError):subject.validate(D,'talking_head_full_1080x1920',M['subject_framing']['face_box'])
        with self.assertRaises(ValueError):subject.validate(D,'full_cutaway_subject_or_product_1080x1920')
    def test_plan_positive(self):self.assertEqual(manifest.validate(M,D),'video')
    def test_plan_empty_objects_fail(self):
        for key in ['source','technical','content_assessment','route_decision','placement_plan','build_plan','export']:
            m=copy.deepcopy(M);m[key]={}
            with self.subTest(key=key),self.assertRaises((ValueError,KeyError)):manifest.validate(m,D)
    def test_plan_unsafe_geometry_and_time(self):
        for changes in [{'rect':{'x':0,'y':0,'w':9999,'h':9999}},{'start':-1},{'end':1000},{'end':float('nan')},{'start':3,'end':2}]:
            m=copy.deepcopy(M);m['placement_plan']['overlays'][0].update(changes)
            with self.subTest(changes=changes),self.assertRaises(ValueError):manifest.validate(m,D)
    def test_plan_face_overlap_fails(self):
        m=copy.deepcopy(M);m['placement_plan']['overlays'][0]['rect']={'x':350,'y':600,'w':200,'h':100}
        with self.assertRaises(ValueError):manifest.validate(m,D)
    def test_plan_wrong_anchor_or_rtl_rejected(self):
        for key,value in [('anchor',True),('direction','rtl'),('platform','meta')]:
            m=copy.deepcopy(M);m['placement_context'][key]=value
            with self.subTest(key=key),self.assertRaises(ValueError):manifest.validate(m,D)
    def test_forged_qc_is_not_completion(self):
        m=copy.deepcopy(M);m['qc']={'safe_zone_pass':True,'export_pass':True};path=self.out/'plan.json';path.write_text(json.dumps(m));result=self.run_cli('check-production-manifest',path)
        self.assertEqual(result.returncode,0);self.assertIn('PLAN only',result.stdout);self.assertIn('NOT verified',result.stdout)
    def test_static_plan_needs_no_video_export(self):
        m=copy.deepcopy(M);route=D['route_decision']['routes']['carousel_static'];m['route_decision']={'route':'carousel_static',**{k:route[k] for k in ['renderer_skill','content_style']},'reason':'Fictional still'};m['safe_zone_profile']='feed_carousel_4x5_1080x1350_center80';m['technical']={'width':1080,'height':1350};m['placement_context']={'platform':'local_composition_preset','evidence':'Fictional crop plan'};m.pop('subject_framing');m['placement_plan']={'overlays':[]};m['export']={'profile':'carousel_feed_static','format':'png'}
        self.assertEqual(manifest.validate(m,D),'static')
    def test_json_nan_rejected(self):
        p=self.out/'bad.json';p.write_text('{"x":NaN}')
        with self.assertRaises(ValueError):load_json(p)
    def test_mp4_faststart_uses_boxes(self):
        p=self.out/'ok.mp4';p.write_bytes(FTYP+box(b'moov')+box(b'mdat',b'moov'))
        self.assertTrue(export.moov_before_mdat(p))
        p.write_bytes(FTYP+box(b'free',b'moov')+box(b'mdat')+box(b'moov'));self.assertFalse(export.moov_before_mdat(p))
    def test_invalid_mp4_rejected(self):
        for content in [b'xxxxxxxxmoovxxxxmdat',FTYP+struct.pack('>I4s',999,b'moov'),FTYP+box(b'moov')+b'xxx']:
            p=self.out/'bad.mp4';p.write_bytes(content)
            with self.subTest(content=content),self.assertRaises(ValueError):export.moov_before_mdat(p)
    def test_extended_size_and_sparse_large_file(self):
        p=self.out/'large.mp4'
        with p.open('wb') as f:
            f.write(FTYP);f.write(struct.pack('>I4sQ',1,b'free',70_000_000));f.seek(len(FTYP)+70_000_000);f.write(box(b'moov')+box(b'mdat'))
        with patch.object(Path,'read_bytes',side_effect=AssertionError('whole file read')):self.assertTrue(export.moov_before_mdat(p))
    def test_export_positive_and_silent_intent(self):
        self.assertEqual(export.validate(probe(),PROFILE)['video_mbps'],8)
        p=probe();p['streams'].pop()
        with self.assertRaises(ValueError):export.validate(p,PROFILE)
        self.assertEqual(export.validate(p,PROFILE,allow_silent=True)['audio_streams'],0)
    def test_audio_cannot_inflate_video_bitrate(self):
        p=probe();p['streams'][0]['bit_rate']='1000000'
        with self.assertRaises(ValueError):export.validate(p,PROFILE)
    def test_missing_metadata_fails(self):
        for key in ['bit_rate','pix_fmt','field_order','sample_aspect_ratio','color_space','color_transfer','color_primaries','avg_frame_rate']:
            p=probe();p['streams'][0].pop(key)
            with self.subTest(key=key),self.assertRaises(ValueError):export.validate(p,PROFILE)
    def test_bad_audio_fps_color_rejected(self):
        for target,key,value in [(0,'avg_frame_rate','30/1'),(0,'color_space','bt2020nc'),(0,'field_order','tt'),(1,'sample_rate','44100'),(1,'channels',6),(1,'bit_rate','64000'),(1,'codec_name','mp3')]:
            p=probe();p['streams'][target][key]=value
            with self.subTest(key=key),self.assertRaises(ValueError):export.validate(p,PROFILE)
        with self.assertRaises(ValueError):export.validate(probe(),PROFILE,source_fps=30)

if __name__=='__main__':unittest.main(verbosity=2)
