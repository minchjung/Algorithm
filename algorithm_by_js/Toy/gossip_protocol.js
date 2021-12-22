const gossipProtocol = function (village, row, col) {
  // TODO: 여기에 코드를 작성합니다.
	let dirR = [1,-1,0,0], dirC = [0,0,1,-1];
	let board = village.map(ele => ele.split("").map(numStr => Number(numStr)));
// 
	let Q = [[row,col,0]];
	ans = 0;
	while(Q.length > 0){
		const [r,c,t] = Q.shift();
		for(let i = 0 ; i < 4; i++){
			const [nxtR, nxtC, nxtT] = [r + dirR[i], c + dirC[i], t +1];
			if(nxtR < 0 || nxtC < 0 || nxtR >= board.length || nxtC >= board[0].length) continue; 
			if(board[nxtR][nxtC] === 0) continue;
			board[nxtR][nxtC] = 0;
			Q.push([nxtR,nxtC,nxtT]);
			ans = Math.max(ans, nxtT);
		}
	}
	return ans;
};

let village = [
  '0101', // 첫 번째 줄
  '0111',
  '0110',
  '0100',
];
let row = 1;
let col = 2;
let output = gossipProtocol(village, row, col);
console.log(output); // --> 3
