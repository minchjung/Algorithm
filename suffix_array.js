let fs = require("fs");
let input = fs.readFileSync("dev/stdin").toString().trim().split("\n");
const str= input[0]
// const str = 'abracadabra'
const N = str.length; 
sa = [] 

for(let i = 0 ; i < N ; i++){
  let obj = {idx : 0, rank : 0, nextRank : 0}
  obj.idx = i 
  obj.rank = str.substring(i).charCodeAt(0) - 'a'.charCodeAt(0)
  sa.push(obj)
}
for(let i = 0 ; i < N -1; i++){
  sa[i].nextRank = sa[i+1].rank
}
sa[N-1].nextRank = -1
sa.sort((a,b)=> a.rank - b.rank || a.nextRank - b.nextRank)

let tem = new Array(N).fill(0)
for(let d = 4; d < 2*N ; d <<=1){
  let rank = 0
  let prev = sa[0].rank;
  sa[0].rank = 0; 
  tem[sa[0].index] = 0;
  
  for(let i = 1 ; i < N ; i++){
    if(prev === sa[i].rank && sa[i-1].nextRank === sa[i].nextRank){
      prev = sa[i].rank ;
      sa[i].rank = rank;
    }
    else{
      prev = sa[i].rank;
      sa[i].rank = ++rank;
    } 
    tem[sa[i].idx] = i;
  }
  for(let i = 0 ; i < N ; i++){
    let nextIdx = sa[i].idx + Math.ceil(d/2);
    if(nextIdx >= N){
      sa[i].nextRank = -1;
      continue 
    }
    sa[i].nextRank = sa[tem[nextIdx]].rank;
  }
  sa.sort((a,b)=> a.rank - b.rank || a.nextRank - b.nextRank)
}

const LCP = (str, suffix) =>{
  const N = suffix.length
  let lcp = new Array(N).fill(0);
  let inv = new Array(N).fill(0);

  for(let i = 0 ; i < N ; i++)  inv[suffix[i]] = i
  
  let k = 0 ; 
  for(let i = 0 ; i < N ; i++){
    if(inv[i] === N -1){
      k = 0;
      continue;
    }
    let j = suffix[inv[i] + 1];
    while(i + k < N && j + k < N){
      if(str[i + k] !== str[j + k]) break;
      k++;
    }
    lcp[inv[i]] = k;
    if(k > 0) k --;
  }
  lcp.unshift('x')
  return lcp;
}
const lcp = LCP(str, sa.map(ele => ele.idx))
console.log(sa.map(ele=> ele.idx +1).join(" "))
console.log(lcp.join(" "))