const robotPath2 = function (room, src, sDir, dst, dDir) {
  // TODO: 여기에 코드를 작성합니다.
	// 위쪽이 1, 오른쪽이 2, 
	// 아래쪽이 3, 왼쪽이 4
	const OOB = (row, col) =>  //경계면 탐색
		row < 0 || col < 0 || 
		row >= room.length || col >= room[0].length; 

	const getMovement =(cur, nxt) => //방향전환시 이동 횟수 
		cur[0] === nxt[0] && cur[1] ===nxt[1] ? 0 
		: cur[0]*nxt[0] + cur[1]*nxt[1] === 0 ? 2 : 3

	const getCoordinate = (num)=>{ // 방향 결정
		let dir = [0,0];
		switch(num){
			case 1 : 
				dir[0]--;
				break;
			case 2 : 
				dir[1]++;
				break;
			case 3 : 
				dir[0]++;
				break;
			case 4 : 
				dir[1]--;
				break;
		}
		return dir;
	}
	
	let dirX = [1,-1,0,0];
	let dirY = [0,0,1,-1];
	let board = room.map(ele => ele.map( spot => spot === 1 ? 'x' : spot ));
	board[src[0]][src[1]] ='s';
	
  // Q = [row, col, [-1,0 <-현재 이동방향], 누적 동작수]
	let Q = [[...src.slice(),getCoordinate(sDir), 0]];
	let ans = 0; 
	while(Q.length > 0){
		let [r,c,curD,m] = Q.shift(); //현재 좌표, [이동방향], 누적 동작수
		if(r === dst[0] && c === dst[1]){ // 목표지점 도달
			const targetD = getCoordinate(dDir)
      ans = m +getMovement(curD, getCoordinate(dDir)) -1; // 필요 방향 회전 이동수 count 
			if(curD[0] === targetD[0] && curD[1] === targetD[1]) ans++; // 일치하면 함수 return 0 이므로 +1 필요
			break;
		}
		for(let i = 0 ; i < 4; i++){ // 상하좌우 탐색
			const nxtD = [dirX[i], dirY[i]]; // 다음 방향
			const [nxtR, nxtC] = [ r + nxtD[0], c + nxtD[1]]; // 다음 좌표
			if(OOB(nxtR, nxtC)) continue; // 좌표 경계면 벗어나거나
			if(board[nxtR][nxtC] !== 0) continue; // 가본 곳이 아니면 continue

			let move = getMovement(curD, nxtD); // 방향 전환시 필요 이동 횟수
			if(nxtD[0] === curD[0] && nxtD[1] === curD[1] && board[r][c]==='s') move++;
      // 만약 첫 시작에서 직진 카운트 +1 필요
			board[nxtR][nxtC] = m+move; // board 동작수 기록
			Q.push([nxtR, nxtC,nxtD, m+move]); // Q push [다음좌표, 다음이동방향, 누적이동수]
		}
		Q.sort((a,b)=>(a[3]-b[3])) // 최소 거리위해  누적 이동수 오름차순 정렬
	}
	return ans
};