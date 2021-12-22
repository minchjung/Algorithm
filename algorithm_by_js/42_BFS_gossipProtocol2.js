const createMatrix = (village) => {
  const matrix = [];
  village.forEach((line) => {
    const row = [];
    for (let i = 0; i < line.length; i++) row.push(Number(line[i]));
    matrix.push(row);
  });
  return matrix;
};

const gossipProtocol2 = function (village, num) {
  // TODO: 여기에 코드를 작성합니다.
  let arr = []
  const R = village.length;
  const C = village[0].length;
  // Get the cㅁandidated one that has '2'
  for(let i = 0 ; i < R; i++){
    for(let j = 0 ; j < C; j++){
      if(village[i][j] === "2") arr.push([i,j])
    }
  }

  // Get the combination of candidated 
  // ex) all candidated,'2', is 5 
  //     , and pick 3 among them
  //     => 5C3
  let comb =[]
  let vis = new Array(arr.length).fill(false);
  const getCombination = (k, s, basket) => {
    if(k === num)
      return comb.push(basket.slice())

    for(let i =s ; i < arr.length; i++){
      if(vis[i]) continue ;
      vis[i] = true;
      basket[k] = arr[i]
      getCombination(k+1, i+1, basket)
      vis[i] = false;
    }
  }
  getCombination(0,0, new Array(num).fill(0))
 
  const dirR = [0,0,1,-1];
  const dirC = [1,-1,0,0];
  let ans = 1e10 ;

  // Search shortest time-cost to spread them all
  for(let candidate of comb){ 
    let vis = new Array(R).fill(0).map( () => new Array(C).fill(false))
    let Q =[]
    let matrix = new Array(R).fill(0).map( () => new Array(C).fill(0))
    // push the picked all into Q 
    for(let cand of candidate)
      Q.push([...cand, 0])
    // BFS
    while(Q.length > 0){
      const [ r, c, t] = Q.shift();
      vis[r][c] = true;
      for(let d = 0 ; d < 4; d++){
        const [ nxtR, nxtC ] = [ r + dirR[d], c + dirC[d] ]
        if( nxtR < 0 || nxtC < 0 || nxtR >= R || nxtC >= C) continue; 
        if( vis[nxtR][nxtC] || village[nxtR][nxtC] === '0') continue;
        vis[nxtR][nxtC] = true; 
        matrix[nxtR][nxtC] = t + 1;
        Q.push([nxtR, nxtC, t+1])
      }
    }
    // Check if it's all spreaded out
    let checkAll =true
    for(let i = 0 ; i < R; i++){
      if(!checkAll) break;
      for(let j = 0 ; j < C; j++){
        if(vis[i][j] === false && village[i][j] == '1'){
          checkAll = false; 
          break
        }
      }
    }
    // if its true, Get the spent-time 
    if(!checkAll) continue;  
    let maxTime = 0 ;
    for(let i = 0 ; i < R; i ++){
      for(let j = 0 ; j < C ; j++){
        if(village[i][j] ==  '1') maxTime =Math.max(maxTime, matrix[i][j])
      }
    }
    // Get Min answer, update each BFS 
    ans = Math.min(ans, maxTime)
  }

  return ans
};
