const rotateMatrix = function (matrix, c=1) {
	// TODO: 여기에 코드를 작성합니다.
  c %= 4;
	while (c-- && matrix.length !== 0){
		const N = matrix.length;
		const M = matrix[0].length;
		let ref = new Array(M).fill(0).map(ele => new Array(N))
	
		for(let r = 0; r < N; r++){
			for(let c = 0; c < M; c++)
				ref[c][N-1-r] = matrix[r][c];
		}
		matrix = ref.map(ele => ele.slice());
	}
	return matrix
};