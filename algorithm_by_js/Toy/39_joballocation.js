const jobAllocation = function (jobs, workersNum) {
  // TODO: 여기에 코드를 작성합니다.
  const N = jobs.length;
  let dp = new Array(N).fill(0).map(()=> new Array(N).fill(-1));
  let Q = [[0, workersNum-1, 0]] // start, left cnt to divide, tot-max 
  let ans = 1e11;
  dp[0][0] = jobs[0]; // Memo to start

  while(Q.length > 0){
    const [s, cnt, tot] = Q.shift();
    if(cnt === 0){ 
      dp[s][N-1] = s === N - 1  // cur start = the last?
        ? jobs[N-1] // just give the last value
        : dp[s][N-1] // already had one in memo ?
        ? dp[s][N-1] // just give it
        : dp[s][N-2] + jobs[N-1]  // none of them above? 
        // we can calculate that sum of the last value(jobs[N-1])
        // with the one on memo, just right before   
      ans = Math.min(ans, Math.max(dp[s][N-1], tot)) // Get the answer
      continue;
    }
    let curSum=0
    for(let i = s; i < N - cnt; i++){
      curSum += jobs[i]; 
      dp[s][i] = curSum
      Q.push([i+1, cnt-1, Math.max(tot, curSum)])
    }
  }
  return ans
};
// It works but Not O[MN];
// Need to fine tune more
