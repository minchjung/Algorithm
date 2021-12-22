const coinChange = function (total, coins) {
	// TODO: 여기에 코드를 작성합니다.
	const N = coins.length;
	const M = total + 1;
	let dp = new Array(N).fill(0).map(ele => new Array(M).fill(0))
	
	for(let i = 0 ; i < N; i++){
		for(let j = 0 ; j < M; j++){
			if(j === 0) dp[i][j] =1;
			else if(j < coins[i] )
				dp[i][j] = i !== 0 ? dp[i-1][j] : 0
			else 
				dp[i][j] = i !== 0 
				? dp[i][j -coins[i]] + dp[i-1][j]
				: dp[i][j -coins[i]]
		}
	}
	return dp[N-1][M-1]
}
// This is what I solved for tabulate DP 
// 1. Set column as target like 0 ~ Target  
// 2. Set row as coins (ascending) 
//    since we examine from the bottom 
// 3. Get all optimized solution 
//    [ if coin > target ] 0 (no solution)
//    [ if coin == target ] 1 (only one solution)
//    [ if coin < target ] 0 or 1 (need to find out more)
//       lets say subtarget = target- coin 
//       [ if coin > subtarget ] 0
//       [ if coin == subtarget ] 1
//       [ if coin < subtarget] 0 or 1 (again !!)
//        ...
// 4. With That Logic, we can go for it by recursive or by Greedy-dp  
