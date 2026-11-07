# Remove the "A Note to Gifts" page (first card of the last section) and pull the rest up
import re
from bs4 import BeautifulSoup
h=open('home.html',encoding='utf-8').read()
s=BeautifulSoup(h,'lxml')
REMOVE=['LBcyfXSVBJmq4nFL','LBFC3mkzwBGS2b00','LB1M51PzB5qzfw4C','LBmncgxRrbMqw2v5','LB4FVHvXK08X90Yd','LBBnjg9WYjJlNZRc','LBpCsX8kskjjkdpL','LBKDQhwkhj4kzqRJ']
for i in REMOVE:
    el=s.find(id=i)
    if el: el.decompose()
SHIFT=1303.0
sec=s.find_all('section')[3]
c=sec.select('._mXnjA')[0]
for ch in c.find_all(recursive=False):
    st=ch.get('style','')
    m=re.search(r'translate\(([-\d.e]+)px, ([-\d.e]+)px\)',st)
    if m and ch.get('id') not in (None,):
        y=float(m.group(2))-SHIFT
        ch['style']=st.replace(m.group(0),f'translate({m.group(1)}px, {y:.3f}px)')
OLD='3927.09px'; NEW=f'{3927.09-SHIFT:.2f}px'
for el in sec.find_all(style=True):
    if OLD in el['style']: el['style']=el['style'].replace(OLD,NEW)
    el['style']=re.sub(r'(position: absolute; top: 93.8px; left: 93.8px; width: 750.4px; height: )([\d.]+)px',lambda m:m.group(1)+f'{float(m.group(2))-SHIFT:.2f}px',el['style'])
open('home.html','w',encoding='utf-8').write(str(s))
print('ok',NEW)
