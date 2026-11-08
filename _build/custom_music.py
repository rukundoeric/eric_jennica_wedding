# Music: own audio player (music/wedding-song.mp3) that starts automatically when the browser
# allows it, otherwise on the first tap. Falls back to the YouTube player if the mp3 is missing.
h=open('home.html',encoding='utf-8').read()
old='src="https://www.youtube-nocookie.com/embed/MwBXVgR6Es4"'
assert h.count(old)==1
h=h.replace(old,'id="ytmusic" src="https://www.youtube-nocookie.com/embed/MwBXVgR6Es4?playsinline=1"')
css='''<style>
html{-webkit-text-size-adjust:none;text-size-adjust:none}
#LBPpttj7jqPwnLvP{display:none}
#LBPpttj7jqPwnLvP.yt-on{display:block}
.mhint{position:fixed;left:50%;top:14px;transform:translate(-50%,-20px);opacity:0;pointer-events:none;z-index:50;background:#6d0815;color:#fcdb79;font:600 14px/1 'Noto Serif',serif;letter-spacing:1px;padding:12px 20px;border-radius:30px;box-shadow:0 6px 18px rgba(80,20,0,.35);transition:opacity .4s,transform .4s;white-space:nowrap}
.mhint.on{opacity:1;transform:translate(-50%,0);pointer-events:auto}
#LBBmpGZ4qr2Xk4P8{cursor:pointer;-webkit-tap-highlight-color:transparent}
#LBBmpGZ4qr2Xk4P8.playing{animation:mpulse 2.4s ease-in-out infinite}
@keyframes mpulse{50%{filter:drop-shadow(0 0 10px rgba(219,169,78,.9))}}
</style>'''
h=h.replace('</head>',css+'</head>',1)
js='''<script>
(function(){
  var SRC='music/wedding-song.mp3';
  var host=null; try{ if(window.parent!==window && window.parent.WeddingMusic) host=window.parent.WeddingMusic; }catch(e){}
  var A, state;
  if(host){ A=host.audio; state=host; }
  else { A=new Audio(SRC); A.loop=true; A.preload='auto'; A.setAttribute('playsinline',''); state={userPaused:false}; }
  var btn=document.getElementById('LBBmpGZ4qr2Xk4P8'), img=btn&&btn.querySelector('img');
  var PLAY=img?img.src:'', PAUSE="data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='50' r='48' fill='%236d0815'/%3E%3Crect x='35' y='30' width='10' height='40' rx='2' fill='%23fcdb79'/%3E%3Crect x='55' y='30' width='10' height='40' rx='2' fill='%23fcdb79'/%3E%3C/svg%3E";
  var yt=false;
  function ui(){ if(!img||yt) return; img.src=A.paused?PLAY:PAUSE; btn.classList.toggle('playing',!A.paused); }
  function fallback(){ // no mp3 -> use the YouTube player over the button, as before
    if(yt) return; yt=true; document.getElementById('LBPpttj7jqPwnLvP').classList.add('yt-on'); off(); }
  A.addEventListener('play',ui); A.addEventListener('pause',ui);
  A.addEventListener('error',fallback);
  function tryPlay(){ if(host&&!host.opened) return; if(yt||state.userPaused||!A.paused) return; var p=A.play(); if(p&&p.catch) p.catch(function(){}); }
  if(btn) btn.addEventListener('click',function(e){
    if(yt) return; e.stopPropagation();
    if(A.paused){ state.userPaused=false; A.play().catch(function(){}); } else { state.userPaused=true; A.pause(); }
  });
  // start straight away if allowed, otherwise on the first tap / key press anywhere
  var evs=['touchend','click','keydown'];
  function kick(e){ if(btn&&btn.contains(e.target)) return; tryPlay(); }
  function off(){ evs.forEach(function(t){document.removeEventListener(t,kick,true);}); }
  evs.forEach(function(t){document.addEventListener(t,kick,true);});
  var hint=document.createElement('div'); hint.className='mhint'; hint.innerHTML='&#9835;&nbsp; Tap anywhere to play the music'; document.body.appendChild(hint);
  hint.addEventListener('click',function(){ tryPlay(); });
  function showHint(){ if(!yt && A.paused && !state.userPaused && (!host||host.opened)) hint.classList.add('on'); }
  A.addEventListener('playing',function(){ off(); hint.classList.remove('on'); });
  A.addEventListener('pause',function(){ hint.classList.remove('on'); });
  
  if(A.error) fallback();
  ui(); tryPlay();
})();
</script>'''
h=h.replace('</body>',js+'</body>',1)
open('home.html','w',encoding='utf-8').write(h)
print('music ok')
