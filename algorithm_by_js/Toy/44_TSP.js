function calculateDistance(p1, p2) {
  const yDiffSquared = Math.pow(p2[0] - p1[0], 2);
  const xDiffSquared = Math.pow(p2[1] - p1[1], 2);
  const dist = Math.sqrt(yDiffSquared + xDiffSquared);
  return Math.floor(dist * 100);
}

const TSP = function (places) {
  // TODO: 여기에 코드를 작성합니다.
  const INF = 1e10
  const N = places.length;
  
  let vis = new Array(N).fill(false);
  let ans = INF

  const DFS = (k, node, tot) => {
    if(k === N-1){
      ans = Math.min(ans, tot)
      return 
    }

    for(let i = 0 ; i < N; i ++){
      if(vis[i]) continue; 
      const nxt = tot + calculateDistance(places[node], places[i])
      vis[i] = true 
      DFS(k+1, i, nxt)
      vis[i] = false
    }
  }
  for(let i = 0 ; i < N; i++){
    vis = new Array(N).fill(false)
    vis[i] = true
    DFS(0,i,0)
  }
  // console.log(ans)
  return ans
};
