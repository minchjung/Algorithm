const LSCS = function (arr) {
  //TODO: 여기에 코드를 작성합니다.
	let dp = new Array(arr.length).fill(0);
	dp[0] = arr[0];
	
	let ans = -1e10;
	for(let i = 1 ; i < arr.length ; i++){
		dp[i] = Math.max(0, dp[i-1]) + arr[i]
		ans = Math.max(ans, dp[i])
	}
	return ans;
};
