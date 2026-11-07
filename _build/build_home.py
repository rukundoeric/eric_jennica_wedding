import re, csv, os
h=open('_build/home.snapshot.html',encoding='utf-8').read()
# --- asset mapping: original hash file -> best local file ---
m={}
for r in csv.DictReader(open('index.csv')):
    p=r['new_path']
    if '/_lower-res/' in p:
        d,f=p.split('/_lower-res/'); base=re.sub(r'_\d+x\d+(\.\w+)$',r'\1',f); main=f'{d}/{base}'
        m[r['original_file']]=main if os.path.exists(main) else p
    else: m[r['original_file']]=p
miss=set()
def rep(mo):
    f=mo.group(1)
    if f in m: return m[f]
    miss.add(f); return mo.group(0)
h=re.sub(r'(?:https://juaninkandcrafts\.my\.canva\.site)?/?(?:eric-jennica-wedding/)?_assets/media/([0-9a-f]{32}\.[a-z0-9]+)',rep,h)
# --- fonts ---
fonts={'YACgEWqX9J4_0':"'Old Standard TT', serif",'YACgEdYQidM_0':"'Noto Serif', serif",'YADK4JHqBpg_0':"'Noto Serif', serif",
       'YADZ-VrK7PA_0':"'Licorice', cursive",'YACgEX27qLg_0':"'Great Vibes', cursive"}
for k,v in fonts.items(): h=h.replace(k+', auto',v).replace(k,v)
gf='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Licorice&family=Noto+Serif:ital,wght@0,400;0,700;1,400;1,700&family=Old+Standard+TT:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">'
# --- misc fixes ---
h=re.sub(r'url\("?images/[0-9a-f]{32}\.\w+"?\)','none',h)
h=h.replace('src="//www.youtube-nocookie.com','src="https://www.youtube-nocookie.com')
h=re.sub(r'src="https://canva-embed\.com/api/iframe\?[^"]*"','src="https://maps.google.com/maps?q=Merryland%20Pavilion%2C%207%20Rizal%20Street%2C%20Pulilan%2C%20Bulacan&amp;z=16&amp;output=embed"',h)
play='data:image/svg+xml;utf8,'+"%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='50' r='48' fill='%236d0815'/%3E%3Cpath d='M40 30 L72 50 L40 70Z' fill='%23fcdb79'/%3E%3C/svg%3E"
h=re.sub(r'src="blob:[^"]*"',f'src="{play}"',h)
h=re.sub(r'href="(?:https://juaninkandcrafts\.my\.canva\.site)?/eric-jennica-wedding/?"','href="index.html"',h)
# remove canva footer: find element containing policies links
i=h.find('https://www.canva.com/policies/terms-of-use/')
if i>0:
    fs=h.rfind('<footer',0,i)
    if fs>0:
        fe=h.find('</footer>',i)+9; h=h[:fs]+h[fe:]
h=h.replace(' crossorigin="anonymous"','')
def cut_div(h,marker):
    i=h.find(marker)
    if i<0: return h
    j=i; depth=0
    import re as _re
    for mo in _re.finditer(r'<div\b|</div>',h[i:]):
        depth+=1 if mo.group(0)=='<div' else -1
        if depth==0: j=i+mo.end(); break
    return h[:i]+h[j:]
h=cut_div(h,'<div class="footer-overflow-container"')
# title/meta + scaling
head_add=gf+'''<meta name="viewport" content="width=device-width, initial-scale=1"><title>Eric &amp; Jennica Wedding</title>
<style>html,body{margin:0;background:#fcdb79}</style>'''
h=h.replace('<head>','<head><meta charset="utf-8">'+head_add,1)
scale='''<script>(function(){var W=938;function fit(){var z=window.innerWidth/W;var c=document.querySelector('.KYQZFA');if(c)c.style.zoom=z;}window.addEventListener('resize',fit);fit();})();</script>'''
h=h.replace('</body>',scale+'</body>')
open('home.html','w',encoding='utf-8').write(h)
print('missing assets:',len(miss),list(miss)[:5]); print('size',len(h))
