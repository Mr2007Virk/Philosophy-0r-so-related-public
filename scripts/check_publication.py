#!/usr/bin/env python3
"""Validate that the public showcase contains only its fictional demo dataset."""
from pathlib import Path
import hashlib, json, sys
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'data'/'integrity-manifest.json').read_text(encoding='utf-8'))
data_path=ROOT/'data'/'demo-archive.json'
actual=hashlib.sha256(data_path.read_bytes()).hexdigest()
if actual != manifest.get('sha256'):
    print('FAIL: demo dataset fingerprint does not match manifest'); sys.exit(1)
data=json.loads(data_path.read_text(encoding='utf-8'))
if data.get('dataset_type') != 'fictional_demo_only':
    print('FAIL: dataset is not marked fictional_demo_only'); sys.exit(1)
for rec in data.get('records',[]):
    if not str(rec.get('id','')).startswith('DEMO-') or not str(rec.get('source_id','')).startswith('DEMO-'):
        print('FAIL: non-demo record/source identifier detected'); sys.exit(1)
for forbidden in ['philosophy_archive.sqlite3','owner_pin.txt','Philosophy_Books_Verbatim_v3.json','Structured archive and handoff']:
    if any(forbidden.lower() in p.name.lower() for p in ROOT.rglob('*')):
        print('FAIL: private archive material in public package:', forbidden); sys.exit(1)
print('PASS: public dataset hash, fictional markers and privacy file checks verified.')
