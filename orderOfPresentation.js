function orderOfPresentation (N, K) {
  const addFact = (n) => n <= 1 ? 1 : n * addFact(n-1)
  const countFalse = (arr) => {
    return arr.reduce( (tot, ele) => 
      ele === false ? tot+1 : tot
    ,0)
  }
  let isUsed = new Array(N+1).fill(false);
  let ans = 0;
  for(let i = 0 ; i < N ; i ++){
    isUsed[K[i]] = true; 
    ans += countFalse(isUsed.slice(1,K[i])) * addFact( countFalse(isUsed)-1)
  }
  return ans
}