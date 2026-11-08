# On tall/narrow screens (phones) stretch the Save the Date section so it fills the first screen.
# --x = extra height in design px (0 on wide screens); everything below moves down by --x.
h=open('home.html',encoding='utf-8').read()
SHIFT=['LBRkQH5fgJwKqSc9','LBBmpGZ4qr2Xk4P8','LBPv47VJJmxjD19n','LBzdVBSWjwf9BnWN','LBFdngjY211VvCD5',
       'LB0LlBKSDmRJmm3p','LBTfQgzP7HSHJhnn','LB3MZS577pfB7fTf','LBmlm2CcJWQKMXkM','LBPpttj7jqPwnLvP']
H0='5408.47px'
assert h.count(H0)==4, h.count(H0)
h=h.replace(H0,f'calc({H0} + var(--x, 0px))')
css='<style>\n'+','.join('#'+i for i in SHIFT)+'{translate:0 var(--x,0px)}\n'+'''.tline{top:calc(1530px + var(--x,0px))}
.std{height:calc(945.6px + var(--x,0px));background:#faf0e3 url("01_save-the-date/std-background-tall.jpg") 0 0/100% auto no-repeat}
.std .t1{top:calc(78px + var(--x,0px)*.16)}
.std .t2{top:calc(158px + var(--x,0px)*.18)}
.std .arch{top:calc(212px + var(--x,0px)*.21);width:calc(346px + var(--x,0px)*.2);height:calc(452px + var(--x,0px)*.42);
           margin-left:calc(-173px - var(--x,0px)*.1);border-radius:999px 999px 0 0}
.std .arch div{border-radius:999px 999px 0 0}
.std .names{top:calc(680px + var(--x,0px)*.68)}
.std .div{top:calc(772px + var(--x,0px)*.72)}
.std .date{top:calc(790px + var(--x,0px)*.72)}
</style>'''
h=h.replace('</head>',css+'</head>',1)
js='''<script>(function(){
  // fill the first screen on phones; computed once (and on width change) so it doesn't jump while scrolling
  var lastW=0;
  function grow(){ var w=window.innerWidth; if(w===lastW) return; lastW=w;
    var z=w/938, x=window.innerHeight/z-945.6-60; x=Math.max(0,Math.min(850,x));
    var s=document.querySelector('section'); if(s) s.style.setProperty('--x',x.toFixed(1)+'px'); }
  grow(); window.addEventListener('resize',grow);
})();</script>'''
h=h.replace('</body>',js+'</body>',1)
open('home.html','w',encoding='utf-8').write(h)
print('std tall ok')
