# Redesign of the Save the Date section (matches the animated Save the Date video)
import re
h=open('home.html',encoding='utf-8').read()
HIDE=['LBrzw50WMkQrfqSt','LBwryRqkhMx2cDgp','LBYjdvpGXs6H3FRX','LBTR06yG4yLjSf2B','LBDk5JC4K2XDHRmK','LBk7KmVvcgb6RWzj','LBbF2BHvyZTLwbQY','LBhTjfFQDPgmCKsn']
for i in HIDE:
    h=h.replace(f'<div id="{i}" class="DF_utQ _0xkaeQ" style="',f'<div id="{i}" class="DF_utQ _0xkaeQ" style="display:none;',1)
css='''<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600&family=Cormorant+Garamond:ital,wght@1,500&family=Great+Vibes&display=swap" rel="stylesheet">
<style>
.std{position:absolute;left:0;top:0;width:938px;height:945.6px;background:url("01_save-the-date/std-background.jpg") 0 0/100% 100% no-repeat;overflow:hidden}
.std *{box-sizing:border-box}
.std .t1{position:absolute;left:0;right:0;top:78px;text-align:center;font-family:'Cinzel',serif;font-weight:600;font-size:60px;letter-spacing:12px;color:#6e1a1f;text-shadow:2px 3px 4px rgba(90,40,0,.18)}
.std .t2{position:absolute;left:0;right:0;top:158px;text-align:center;font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:500;font-size:30px;letter-spacing:3px;color:#6e1a1f}
.std .arch{position:absolute;left:50%;top:212px;width:346px;height:452px;margin-left:-173px;border:3px solid #be8c46;border-radius:173px 173px 0 0;padding:10px;box-shadow:0 14px 26px rgba(110,70,30,.28)}
.std .arch div{width:100%;height:100%;border-radius:163px 163px 0 0;border:11px solid #fffcf6;background:#fffcf6 url("01_save-the-date/std-portrait.jpg") center/cover no-repeat;overflow:hidden}
.std .names{position:absolute;left:0;right:0;top:680px;text-align:center;font-family:'Great Vibes',cursive;font-size:64px;line-height:80px;color:#6e1a1f;text-shadow:2px 3px 4px rgba(90,40,0,.2)}
.std .div{position:absolute;left:50%;top:772px;width:300px;margin-left:-150px;height:2px;background:#6e1a1f}
.std .div:after{content:"";position:absolute;left:50%;top:-6px;width:12px;height:12px;margin-left:-6px;background:#6e1a1f;transform:rotate(45deg)}
.std .date{position:absolute;left:0;right:0;top:790px;text-align:center;font-family:'Cinzel',serif;font-weight:600;font-size:34px;letter-spacing:8px;color:#6e1a1f}
@keyframes stdUp{from{opacity:0;transform:translateY(28px)}to{opacity:1;transform:none}}
@keyframes stdIn{from{opacity:0}to{opacity:1}}
.std .t1{animation:stdUp 1s .2s both}.std .t2{animation:stdUp 1s .6s both}
.std .arch{animation:stdUp 1.2s .9s both}.std .names{animation:stdUp 1.1s 1.6s both}
.std .div,.std .date{animation:stdIn 1s 2.1s both}
</style>'''
h=h.replace('</head>',css+'</head>',1)
std='''<div class="std" aria-label="Save the date"><div class="t1">SAVE THE DATE</div><div class="t2">to the wedding of</div><div class="arch"><div role="img" aria-label="Eric and Jennica"></div></div><div class="names">Rukundo Eric &amp; Jennica Catajay</div><div class="div"></div><div class="date">12 · 19 · 2026</div></div>'''
# insert as first DF element child of the first _mXnjA container (so play button, music & later elements paint above it)
i=h.find('<div id="LBrzw50WMkQrfqSt"')
h=h[:i]+std+h[i:]
# section background colour behind it
h=h.replace('id="PBwjWqyRm3fv3wS4" class="rGeu6w" data-scroll-ready="true" style="background-color: rgb(252, 219, 121);"','id="PBwjWqyRm3fv3wS4" class="rGeu6w" data-scroll-ready="true" style="background-color: rgb(250, 240, 227);"',1)
open('home.html','w',encoding='utf-8').write(h)
print('ok')
