# Link preview (WhatsApp, Messenger, Facebook, iMessage, X...) for index.html and home.html
import re
BASE='https://rukundoeric.github.io/eric_jennica_wedding/'
TITLE="Invitation · Eric & Jennica's Wedding · December 19, 2026"
DESC="You are invited! Join us as Rukundo Eric & Jennica Catajay say \"I do\" on Saturday, December 19, 2026 at Merryland Pavilion, Pulilan, Bulacan."
def meta(url):
    t=TITLE.replace('&','&amp;'); d=DESC.replace('&','&amp;').replace('"','&quot;')
    return f'''<!--share-meta-->
<meta name="description" content="{d}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Eric &amp; Jennica Wedding">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}og-image.jpg?v=2">
<meta property="og:image:secure_url" content="{BASE}og-image.jpg?v=2">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Invitation – Rukundo Eric &amp; Jennica Catajay, December 19, 2026">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{BASE}og-image.jpg?v=2">
<link rel="icon" href="02_details/monogram-EJ.webp">
<link rel="apple-touch-icon" href="og-image.jpg">
<!--/share-meta-->'''
for f,url in [('index.html',BASE),('home.html',BASE+'home.html')]:
    s=open(f,encoding='utf-8').read()
    # drop the old Canva preview tags
    s=re.sub(r'<meta content="[^"]*" property="og:[^"]*"/>\n?','',s)
    s=re.sub(r'<meta content="[^"]*" name="(description|twitter:[^"]*)"/>\n?','',s)
    s=re.sub(r'<!--share-meta-->.*?<!--/share-meta-->\n?','',s,flags=re.S)
    i=s.find('</title>')+len('</title>')
    s=s[:i]+'\n'+meta(url)+'\n'+s[i:]
    open(f,'w',encoding='utf-8').write(s)
print('share meta ok')
