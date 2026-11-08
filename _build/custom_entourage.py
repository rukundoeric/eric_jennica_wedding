# Entourage updates: extra principal sponsors, corrected flower-girl names, ceremony time
import re
h=open('home.html',encoding='utf-8').read()
def must(old,new,count):
    global h
    n=h.count(old); assert n==count,(old,n); h=h.replace(old,new)
# ceremony time
must('December 19, 2026 | 1:00 PM','December 19, 2026 | 2:30 PM',2)
# flower girls (Kimberly Rivero removed, spellings corrected)
must('Chrischel Jas<br/>Rejano Chris<br/>Jasmine Rejano<br/>Kimberly Rivero<br/>Aico Jane Lacdao',
     'Chrischel Jas Rejano<br/>Chris Jasmine Rejano<br/>Aicho Jane Lacdao',2)
# additional principal sponsors
must('Mr. Demetrio Geraldino Jr.</span>','Mr. Demetrio Geraldino Jr.<br/>Mr. Jonald Tejoso<br/>Ptr. Leonardo Cada<br/>Mr. Roger Lonzaga</span>',2)
must('Mrs. Celinda Geraldino</span>','Mrs. Celinda Geraldino<br/>Mrs. Nelia Fernandez<br/>Mrs. Luz Tejoso</span>',2)
def resize(id_,f=None,w=None,x=None):
    global h
    i=h.find(f'id="{id_}"'); j=h.find('>',i); k=h.find('>',j+1)
    seg=h[i:k]
    def mul(m): return f'{m.group(1)}{float(m.group(2))*f:.3f}px'
    if f: seg=re.sub(r'(height: )([\d.]+)px',mul,seg)
    if w:  # widen + recentre (outer and inner, inner is unscaled)
        ow=float(re.search(r'width: ([\d.]+)px',seg).group(1))
        sc=float(re.search(r'scale\(([\d.]+)',seg).group(1))
        tx=float(re.search(r'translate\(([-\d.]+)px',seg).group(1))
        seg=re.sub(r'width: [\d.]+px',f'width: {w:.3f}px',seg,count=1)
        seg=re.sub(r'(writing-mode: horizontal-tb; width: )([\d.]+)px',lambda m:f'{m.group(1)}{w/sc:.3f}px',seg)
        seg=seg.replace(f'translate({tx}px',f'translate({tx-(w-ow)/2:.3f}px',1)
    h=h[:i]+seg+h[k:]
resize('LBzBmTkRRPM9HBsF',13/10)   # men column
resize('LBwTXb3LlGl6lmZD',14/12)   # women column
resize('LBdnlrt5gH0MPjg4',3/5,w=320)  # flower girls box: 3 lines, wider
open('home.html','w',encoding='utf-8').write(h)
print('entourage ok')
