# Make a compressed .webp copy of every image the pages use (originals are kept)
import re,os
from PIL import Image
MAXW=1600
refs=set()
for f in ['home.html','index.html']:
    refs|=set(re.findall(r'(0\d_[^"&)\s]+?\.(?:png|jpe?g))',open(f,encoding='utf-8').read()))
before=after=0
for r in sorted(refs):
    if not os.path.exists(r): continue
    out=re.sub(r'\.(png|jpe?g)$','.webp',r)
    if not (os.path.exists(out) and os.path.getmtime(out)>=os.path.getmtime(r)):
        im=Image.open(r); im.load()
        if im.mode not in ('RGB','RGBA'): im=im.convert('RGBA' if 'A' in im.getbands() or 'transparency' in im.info else 'RGB')
        if im.width>MAXW: im=im.resize((MAXW,round(im.height*MAXW/im.width)),Image.LANCZOS)
        im.save(out,'WEBP',quality=80,method=6)
    before+=os.path.getsize(r); after+=os.path.getsize(out)
print(f'images: {len(refs)}  {before/1e6:.1f} MB -> {after/1e6:.1f} MB')
