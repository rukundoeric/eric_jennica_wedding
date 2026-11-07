# Remove the "Maximized invites by Juan Ink and Crafts" credit link
import re
from bs4 import BeautifulSoup
s=BeautifulSoup(open('home.html',encoding='utf-8').read(),'lxml')
els=[]
for t in s.find_all(string=re.compile('MAXIMIZED INVITES',re.I)):
    el=t.find_parent(class_='DF_utQ')
    if el is not None and el not in els: els.append(el)
for a in s.find_all('a',href=re.compile('facebook.com/profile')):
    el=a.find_parent(class_='DF_utQ')
    if el is not None and el not in els: els.append(el)
print([ (e.get('id'), e.get('style','')[:40], e.get_text(' ',strip=True)[:40]) for e in els])
for e in els: e.decompose()
open('home.html','w',encoding='utf-8').write(str(s))
