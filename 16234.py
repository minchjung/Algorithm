from collections import deque 

N,L,R = map( int, input().split() )
board = [ list(map(int, input().split())) for _ in range(N) ] 

dirX = [1,-1,0,0]
dirY = [0,0,-1,1]
done = True

ans = 0 
while done :
  vis = [ [False]*N for _ in range(N) ] 
  done = False
  for i in range(N):
    for j in range(N):
      if vis[i][j] : continue 
      vis[i][j] = True 

      Q = deque() 
      Q.append([i,j])
      
      coordPlace = []
      coordPlace.append([i,j])
      tot = board[i][j] ;

      while Q : 
        curX, curY = Q.popleft()
        for d in range(4):
          nxtX = curX + dirX[d]
          nxtY = curY + dirY[d]
          if nxtX < 0 or nxtX >= N or nxtY < 0 or nxtY >= N : continue  
          if vis[nxtX][nxtY] : continue
          if L > abs(board[nxtX][nxtY] - board[curX][curY]) or abs(board[nxtX][nxtY] - board[curX][curY]) > R : continue    
     
          vis[nxtX][nxtY] = True 
          Q.append([nxtX, nxtY])
          coordPlace.append([nxtX, nxtY])
          tot += board[nxtX][nxtY]
          done = True
      for x,y in coordPlace : 
        board[x][y] = tot//(len(coordPlace))
  ans += 1
print(ans-1)