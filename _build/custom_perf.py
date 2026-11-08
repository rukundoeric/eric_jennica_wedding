# Faster loading: use .webp images, lazy-load below-the-fold content, load YouTube only if needed,
# and give index.html a versioned link to home.html so phones always get the latest version.
import re,os,hashlib
def webpify(s):
    def rep(m):
        w=re.sub(r'\.(png|jpe?g)$','.webp',m.group(1))
        return w if os.path.exists(w) else m.group(1)
    return re.sub(r'(0\d_[^"&)\s]+?\.(?:png|jpe?g))',rep,s)
h=webpify(open('home.html',encoding='utf-8').read())
# lazy-load every <img> except the ones on the first screen (details card, play button area)
EAGER=['LBRkQH5fgJwKqSc9','LBBmpGZ4qr2Xk4P8','LBPv47VJJmxjD19n','LB3MZS577pfB7fTf']
from bs4 import BeautifulSoup
_b=BeautifulSoup(h,'lxml'); keep=set()
for i in EAGER:
    e=_b.find(id=i)
    if e: keep|={im.get('src') for im in e.find_all('img')}
def lazy(m):
    tag=m.group(0); src=re.search(r'src="([^"]*)"',tag)
    if 'loading=' in tag or not src or src.group(1).startswith('data:') or src.group(1) in keep:
        return tag.replace('<img ','<img decoding="async" ',1) if 'decoding=' not in tag else tag
    return tag.replace('<img ','<img loading="lazy" decoding="async" ',1)
h=re.sub(r'<img [^>]*>',lazy,h)
# map: lazy
h=h.replace('<iframe allowfullscreen="allowfullscreen" sandbox','<iframe loading="lazy" allowfullscreen="allowfullscreen" sandbox',1)
# YouTube: only load it if the mp3 is missing
yt='id="ytmusic" src="https://www.youtube-nocookie.com/embed/MwBXVgR6Es4?playsinline=1"'
assert h.count(yt)==1
h=h.replace(yt,'id="ytmusic" data-src="https://www.youtube-nocookie.com/embed/MwBXVgR6Es4?playsinline=1"')
h=h.replace("document.getElementById('LBPpttj7jqPwnLvP').classList.add('yt-on');",
            "var y=document.getElementById('ytmusic'); if(y&&!y.src) y.src=y.getAttribute('data-src'); document.getElementById('LBPpttj7jqPwnLvP').classList.add('yt-on');")
assert 'data-src\')' in h
open('home.html','w',encoding='utf-8').write(h)
# index.html: webp + versioned link to home.html + preload of the first images
v=hashlib.md5(h.encode()).hexdigest()[:8]
s=webpify(open('index.html',encoding='utf-8').read())
s=re.sub(r'src="home\.html(\?v=[0-9a-f]+)?"',f'src="home.html?v={v}"',s)
if 'rel="preload"' not in s:
    s=s.replace('<link rel="preconnect"','<link rel="preload" as="image" href="00_envelope-page/envelope.webp"><link rel="preload" as="image" href="02_details/floral-frame-background.webp">\n<link rel="preconnect"',1)
open('index.html','w',encoding='utf-8').write(s)
print('perf ok, version',v)
