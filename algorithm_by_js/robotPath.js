const robotPath = function (room, src, dst) {
  // TODO: 여기에 코드를 작성합니다.
	const dirX = [1,-1,0,0];
	const dirY = [0,0,-1,1];
	let vis = room.map( ele => new Array(ele.length).fill(false) );

	Q =[[...src.slice(),0]];
	vis[src[0]][src[1]] = true;
	ans = 0;

	while(Q.length > 0){
		const [r,c,d] = Q.shift();
		if(r === dst[0] && c === dst[1]){
			ans = Math.max(ans, d);
		}
		for(let i = 0 ; i < 4; i++){
			const [nxtR, nxtC] = [r + dirX[i], c + dirY[i]];
			if(nxtR < 0 || nxtR >= room.length || nxtC < 0 || nxtC >= room[0].length) continue;
			if(room[nxtR][nxtC]) continue;
			if(vis[nxtR][nxtC]) continue;
			vis[nxtR][nxtC] = true;
			Q.push([nxtR, nxtC, d+1])
		}
	}
	return ans
};
