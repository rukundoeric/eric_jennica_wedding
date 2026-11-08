# New "Wedding Timeline" block between the details card and The Venue
import re
H=520
h=open('home.html',encoding='utf-8').read()
assert h.count('4888.47px')>=4
h=h.replace('4888.47px',f'{4888.47+H:.2f}px')
i=h.find('id="LBmlm2CcJWQKMXkM"'); k=h.find('>',i)
seg=h[i:k]; m=re.search(r'translate\(([-\d.]+)px, ([-\d.]+)px\)',seg)
seg=seg.replace(m.group(0),f'translate({m.group(1)}px, {float(m.group(2))+H:.3f}px)')
h=h[:i]+seg+h[k:]
row=lambda t,e:f'<div class="tr"><div class="tt">{t}</div><div class="td"></div><div class="te">{e}</div></div>'
block=('<div class="tline" id="timeline"><div class="t1">WEDDING TIMELINE</div>'
 '<div class="tdiv"><span></span><i>&#9829;</i><span></span></div><div class="trows"><div class="tbar"></div>'
 +row('2:30 PM','Ceremony')+row('4:00 PM','Cocktails')+row('5:30 PM','Start of Program')+'</div></div>')
j=h.find('<div class="DF_utQ',h.find('id="LBmlm2CcJWQKMXkM"')-200)
j=h.rfind('<div',0,h.find('id="LBmlm2CcJWQKMXkM"'))
h=h[:j]+block+h[j:]
css='''<style>
.tline{position:absolute;left:0;top:1530px;width:938px;height:520px;background:#faf0e3;color:#6d0815;text-align:center;z-index:1}
.tline:before{content:"";position:absolute;inset:26px 34px;border:1.5px solid #c99a4e;border-radius:4px}
.tline:after{content:"";position:absolute;inset:34px 42px;border:1px solid rgba(201,154,78,.55);border-radius:2px}
.tline .t1{position:absolute;left:0;right:0;top:78px;font-family:'Old Standard TT',serif;font-size:46px;letter-spacing:10px;text-shadow:2px 3px 4px rgba(90,40,0,.15)}
.tline .tdiv{position:absolute;left:0;right:0;top:150px;display:flex;align-items:center;justify-content:center;gap:12px;color:#c99a4e;font-size:18px}
.tline .tdiv span{width:120px;height:1.5px;background:#c99a4e}
.tline .tdiv i{font-style:normal}
.tline .trows{position:absolute;left:0;right:0;top:196px}
.tline .tbar{position:absolute;left:468px;top:30px;height:200px;width:2px;background:#c99a4e}
.tline .tr{position:relative;height:100px;display:flex;align-items:center}
.tline .tt{width:420px;text-align:right;font-family:'Old Standard TT',serif;font-size:30px;letter-spacing:3px}
.tline .td{width:18px;height:18px;margin:0 30px 0 21px;border-radius:50%;background:#6d0815;box-shadow:0 0 0 5px #faf0e3,0 0 0 7px #c99a4e;position:relative;z-index:1}
.tline .te{flex:1;text-align:left;font-family:'Great Vibes',cursive;font-size:50px;white-space:nowrap}
</style>'''
h=h.replace('</head>',css+'</head>',1)
open('home.html','w',encoding='utf-8').write(h)
print('timeline ok')
