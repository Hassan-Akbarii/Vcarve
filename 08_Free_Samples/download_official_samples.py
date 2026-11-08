#!/usr/bin/env python3
"""Download original official Vectric samples for personal study. Standard library only.
Creates a separate Official_Downloads folder. Does not generate or run CNC code.
"""
from pathlib import Path
from urllib.request import Request, urlopen
import io, json, zipfile

root=Path(__file__).resolve().parent
data=json.loads((root/'resources.json').read_text(encoding='utf-8'))
for r in data['resources']:
    if 'download' not in r: continue
    dest=root/'Official_Downloads'/r['id']
    dest.mkdir(parents=True,exist_ok=True)
    print('Downloading',r['title'],flush=True)
    try:
        req=Request(r['download'],headers={'User-Agent':'VCarve-Practice-Learning/1.0'})
        with urlopen(req,timeout=60) as response: raw=response.read(30*1024*1024+1)
        if len(raw)>30*1024*1024: raise ValueError('Unexpected archive over 30 MiB')
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            for info in archive.infolist():
                # Extract learning inputs only. No G-code, tool libraries, macros or executables.
                p=Path(info.filename)
                if p.suffix.lower() not in {'.crv','.dxf','.svg','.pdf','.jpg','.jpeg','.png','.txt'}: continue
                if p.is_absolute() or '..' in p.parts: raise ValueError('Unexpected archive path')
                if info.file_size>30*1024*1024: raise ValueError('Unexpected large member')
                target=dest/p.name
                if target.exists(): print('Keeping existing',target.name);continue
                target.write_bytes(archive.read(info))
                print('  saved',target.name,flush=True)
        (dest/'SOURCE.txt').write_text(r['page']+'\n'+r['download']+'\nOriginal Vectric materials. Keep their terms and attribution.\n',encoding='utf-8')
    except Exception as exc:
        print('Could not download:',exc,'\nUse the official project page:',r['page'])
print('Open .crv with File > Open in VCarve. Read the project settings before changing anything.')
