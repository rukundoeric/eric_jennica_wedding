# RSVP becomes its own section ("Guest List Confirmation") with clear wording
import re
from bs4 import BeautifulSoup
h=open('home.html',encoding='utf-8').read()
s=BeautifulSoup(h,'lxml')
FORM='https://docs.google.com/forms/d/e/1FAIpQLSeGXdXXzXhljg88Wtg3u35LGMXz4GU_CNMb75hnvaYC4nqZzw/viewform'
for i in ['__id436','LB1T7pBbvT9H72Xl','LBJCTctnHdkX300Q']:
    e=s.find(id=i); e and e.decompose()
def shift(el,dy):
    st=el['style']; m=re.search(r'translate\(([-\d.e]+)px, ([-\d.e]+)px\)',st)
    el['style']=st.replace(m.group(0),f'translate({m.group(1)}px, {float(m.group(2))+dy:.3f}px)')
for i in ['LBqTKk93PXDL9hf5','LBcyG6WkZgmSP7kr','LBqbk6ZCPzCPhhNt','LB71JqRdxPlD0g6y','LB6V1PZGBxkllgY5']:
    shift(s.find(id=i),193)          # centre the FAQ inside its card
H=625
shift(s.find(id='LBGSv9TCGtw5CxQV'),H)  # push Gentle Reminders down
sec=s.find_all('section')[3]
for el in sec.find_all(style=True):
    el['style']=el['style'].replace('2624.09px',f'{2624.09+H:.2f}px')
    el['style']=re.sub(r'(position: absolute; top: 93.8px; left: 93.8px; width: 750.4px; height: )([\d.]+)px',lambda m:m.group(1)+f'{float(m.group(2))+H:.2f}px',el['style'])
block=BeautifulSoup(f'''<div class="rsvp" id="rsvp">
 <div class="r1">RSVP</div>
 <div class="r2">GUEST LIST CONFIRMATION</div>
 <p class="r3">We have reserved a seat for you and would love to celebrate with you.<br>
 Please confirm whether you will attend using the short form below.</p>
 <a class="rbtn" href="{FORM}" target="_blank" rel="noopener"><span>CONFIRM ATTENDANCE</span></a>
 <p class="r4">It only takes a minute &#8212; thank you!</p>
</div>''','html.parser')
faq=s.find(id='LB5jGlb754v7PwS6')
faq.insert_after(block)
css=s.new_tag('style'); css.string='''
.rsvp{position:absolute;left:0;top:1315px;width:938px;height:625px;background:url("02_details/floral-frame-background.png") 0 0/100% 100% no-repeat;text-align:center;color:#6d0815}
.rsvp .r1{position:absolute;left:0;right:0;top:118px;font-family:'Old Standard TT',serif;font-size:62px;letter-spacing:14px;text-shadow:2px 3px 4px rgba(90,40,0,.15)}
.rsvp .r2{position:absolute;left:0;right:0;top:200px;font-family:'Noto Serif',serif;font-size:22px;letter-spacing:6px}
.rsvp .r3{position:absolute;left:99px;right:99px;top:258px;margin:0;font-family:'Noto Serif',serif;font-style:italic;font-size:20px;line-height:34px}
.rsvp .rbtn{position:absolute;left:50%;top:352px;width:470px;height:87px;margin-left:-235px;background:url("06_attire-guide/image_07.png") center/100% 100% no-repeat;display:flex;align-items:center;justify-content:center;text-decoration:none;transition:transform .2s}
.rsvp .rbtn:hover{transform:scale(1.04)}
.rsvp .rbtn span{font-family:'Noto Serif',serif;font-size:24px;letter-spacing:3px;color:#fbefd6;text-shadow:1px 2px 2px rgba(80,30,0,.45)}
.rsvp .r4{position:absolute;left:0;right:0;top:452px;margin:0;font-family:'Noto Serif',serif;font-style:italic;font-size:18px;opacity:.85}
'''
s.head.append(css)
open('home.html','w',encoding='utf-8').write(str(s))
print('ok')
