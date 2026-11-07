# Gallery: keep only the white-outfit photos, remove the red/yellow-outfit photos and the "see more photos" link
import re
from bs4 import BeautifulSoup
h=open('home.html',encoding='utf-8').read()
REMOVE=['LB5cNTMkDShZpB40','LB3274J9TsnFf9Qx','LBF23xg8TXsqdpHV','LBf7p06FvNfrKynw','LB1R4vKP13ng4jLl','__id132','LByZGP1pGxV2xt8K']
s=BeautifulSoup(h,'lxml')
for i in REMOVE:
    el=s.find(id=i)
    if el: el.decompose()
sec=s.find_all('section')[1]
OLD='3568.66px'; NEW_SEC=1770; NEW_GRP=NEW_SEC-20
for el in sec.find_all(style=True):
    st=el['style']
    if OLD in st: st=st.replace(OLD,f'{NEW_SEC}px')
    if '3548.94px' in st: st=st.replace('3548.94px',f'{NEW_GRP}px')
    if 'background-color: rgb(255, 255, 255)' in st: st=st.replace('background-color: rgb(255, 255, 255)','background-color: rgb(252, 219, 121)')
    if 'height: 3381' in st: st=re.sub(r'height: 3381[\d.]*px',f'height: {NEW_SEC-190}px',st)
    el['style']=st
open('home.html','w',encoding='utf-8').write(str(s))
print('removed', [i for i in REMOVE])
