#!/usr/bin/env python3
# Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠
# Provenance marker: sk-1dt1j8x
"""Measure local MP4 properties against a Selr export target, without uploading."""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import struct
import subprocess
import sys
sys.dont_write_bytecode = True
from safezone_common import DATA,load_json,number

def mp4_boxes(path):
    """Read top-level box headers, seeking across payloads in bounded memory."""
    total=path.stat().st_size;boxes=[]
    with path.open('rb') as f:
        offset=0
        while offset<total:
            if total-offset<8:raise ValueError('truncated MP4 box header')
            f.seek(offset);size,kind=struct.unpack('>I4s',f.read(8));header=8
            if size==1:
                raw=f.read(8)
                if len(raw)!=8:raise ValueError('truncated extended box size')
                size=struct.unpack('>Q',raw)[0];header=16
            elif size==0:size=total-offset
            if size<header or offset+size>total:raise ValueError('invalid MP4 box size')
            boxes.append((kind,offset,size))
            if kind==b'ftyp':
                if size<header+8 or size>4096:raise ValueError('invalid ftyp')
                payload=f.read(size-header)
                brands=[payload[:4]]+[payload[i:i+4] for i in range(8,len(payload),4)]
                if not set(brands)&{b'isom',b'iso2',b'iso5',b'iso6',b'mp41',b'mp42',b'avc1'}:raise ValueError('unsupported MP4 brand')
            offset+=size
    kinds=[x[0] for x in boxes]
    if kinds.count(b'ftyp')!=1 or kinds.count(b'moov')!=1 or b'mdat' not in kinds:raise ValueError('requires ftyp, one moov and mdat boxes')
    return boxes

def moov_before_mdat(path):
    kinds=[x[0] for x in mp4_boxes(path)]
    return kinds.index(b'moov')<kinds.index(b'mdat')

def probe_number(raw,label):
    try:value=float(raw)
    except (ValueError,TypeError):raise ValueError(f'missing/invalid {label}')
    return number(value,label,True)

def rate(raw,label):
    try:value=float(Fraction(str(raw)))
    except (ValueError,ZeroDivisionError):raise ValueError(f'missing/invalid {label}')
    return number(value,label,True)

def validate(probe,profile,allow_silent=False,source_fps=None):
    streams=probe.get('streams',[]);videos=[s for s in streams if s.get('codec_type')=='video'];audios=[s for s in streams if s.get('codec_type')=='audio']
    if len(videos)!=1:raise ValueError('requires exactly one video stream')
    v=videos[0]
    for key,expected in [('codec_name',profile['video_codec']),('pix_fmt',profile['pix_fmt']),('field_order','progressive'),('sample_aspect_ratio','1:1'),('color_space','bt709'),('color_transfer','bt709'),('color_primaries','bt709')]:
        if v.get(key)!=expected:raise ValueError(f'{key} must be {expected}, got {v.get(key)!r}')
    if (v.get('width'),v.get('height'))!=(profile['canvas']['w'],profile['canvas']['h']):raise ValueError('wrong canvas')
    if v.get('tags',{}).get('rotate') not in (None,'0',0) or any(s.get('rotation',0)!=0 for s in v.get('side_data_list',[])):raise ValueError('rotation metadata requires explicit normalization')
    mbps=probe_number(v.get('bit_rate'),'video stream bitrate')/1e6
    if mbps<profile['video_bitrate_mbps']['minimum']:raise ValueError('video stream bitrate below Selr house target (container/audio bitrate cannot substitute)')
    fps=rate(v.get('avg_frame_rate'),'average frame rate');nominal=rate(v.get('r_frame_rate'),'nominal frame rate')
    if abs(fps-nominal)>.05:raise ValueError('frame-rate metadata disagrees; inspect variable-frame-rate source')
    if not any(abs(fps-r)<.07 for r in profile['frame_rates']):raise ValueError('frame rate outside declared house profile')
    if source_fps is not None and abs(fps-number(source_fps,'source fps',True))>.05:raise ValueError('source/output frame rate differs')
    probe_number(probe.get('format',{}).get('duration'),'duration')
    if not audios and not allow_silent:raise ValueError('no audio stream; use --allow-silent only for an intended silent export')
    if len(audios)>1:raise ValueError('multiple audio streams require explicit review')
    for audio in audios:
        if audio.get('codec_name')!=profile['audio_codec']:raise ValueError('audio must be AAC')
        if probe_number(audio.get('sample_rate'),'audio sample rate')!=48000:raise ValueError('audio sample rate must be 48000')
        if audio.get('channels') not in [1,2]:raise ValueError('audio must be mono or stereo')
        kbps=probe_number(audio.get('bit_rate'),'audio bitrate')/1000
        if not 128<=kbps<=384:raise ValueError('audio bitrate outside 128..384kbps house target')
    return {'video_mbps':round(mbps,3),'fps':fps,'audio_streams':len(audios)}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('video',type=Path);p.add_argument('--profile',default='phone_ready_vertical_reel_1080x1920');p.add_argument('--allow-silent',action='store_true');p.add_argument('--source-fps',type=float);p.add_argument('--max-file-mb',type=float,help='explicit verified delivery limit, no scheduler limit assumed');a=p.parse_args()
    try:
        profile=load_json(DATA)['export_profiles'][a.profile]
        if 'canvas' not in profile:raise ValueError('choose a video export profile')
        if not moov_before_mdat(a.video):raise ValueError('moov must precede mdat for faststart')
        size=a.video.stat().st_size/1e6
        if a.max_file_mb is not None and size>number(a.max_file_mb,'max file MB',True):raise ValueError('file exceeds supplied delivery limit')
        result=subprocess.run(['ffprobe','-v','error','-print_format','json','-show_format','-show_streams',str(a.video.resolve())],capture_output=True,text=True,timeout=60)
        if result.returncode:raise ValueError('ffprobe failed; file could not be measured')
        measured=validate(json.loads(result.stdout),profile,a.allow_silent,a.source_fps)
        print(f'PASS measured export properties: {measured}, {size:.2f} MB; visual/audio listening and platform acceptance unverified')
        if a.source_fps is None:print('Source-frame-rate match not checked; supply --source-fps from source probe')
    except (ValueError,KeyError,TypeError,OSError,subprocess.TimeoutExpired) as e:print(f'ERROR: {e}');return 1
    return 0
if __name__=='__main__':sys.exit(main())
