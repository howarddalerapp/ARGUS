// Minimal client-side full-text search using Fuse.js-like fuzzy search
(function(){
  async function init(){
  const res = await fetch('/ARGUS/search_index.json');
    const index = await res.json();
    const options = {keys:['title','content'],threshold:0.4};
    // Simple scoring search (no external Fuse required)
    const input = document.getElementById('search-input');
    const resultsEl = document.getElementById('search-results');
    input.addEventListener('input', function(){
      const q = this.value.trim().toLowerCase();
      resultsEl.innerHTML = '';
      if(!q) return;
      const results = index.map(item=>{
        const score = scoreMatch(item,q);
        return {item,score};
      }).filter(r=>r.score>0).sort((a,b)=>b.score-a.score).slice(0,12);
      if(results.length===0){ resultsEl.innerHTML = '<div class="small">No results</div>'; return }
      results.forEach(r=>{
        const div = document.createElement('div'); div.className='result';
        div.innerHTML = `<h4><a href="${r.item.path}">${r.item.title}</a></h4><p>${snippet(r.item.content,q)}</p>`;
        resultsEl.appendChild(div);
      });
    });

    function scoreMatch(item,q){
      let s=0; const t=item.title.toLowerCase(); const c=item.content.toLowerCase();
      if(t.includes(q)) s+=3;
      const words=q.split(/\s+/);
      words.forEach(w=>{ if(c.includes(w)) s+=1; });
      return s;
    }
    function snippet(text,q){
      const i=text.toLowerCase().indexOf(q);
      if(i===-1) return text.substring(0,140)+'...';
      const start=Math.max(0,i-60); return '...'+text.substring(start,Math.min(text.length,i+120))+'...';
    }
  }
  window.addEventListener('load',init);
})();
