const spiralTraversal = function (matrix) {
	// TODO: 여기에 코드를 작성합니다.
	const [N, M] = [matrix.length, matrix[0].length];
	let ans = "";
	const dfs = (r,rs,re,c,cs,ce) => {
		ans += matrix[r][c]
		if(ans.length === N*M) return 
		if(r === rs && c >= cs && c < ce) c++;
		else if(r >= rs && r < re && c === ce) r++;
		else if(r === re && c > cs && c <= ce) c--;
		else if(r > rs && r <= re && c === cs) r--;
		if(r === rs && c === cs){
			return dfs(r+1,rs+1,re-1,c+1,cs+1,ce-1)
		}
		dfs(r,rs,re,c,cs,ce)
	}
	dfs(0,0,N-1,0,0,M-1)
	return ans
};
