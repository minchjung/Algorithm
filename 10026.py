from collections import deque 

N = int(input())
board = [ list(input()) for _ in range(N) ]
board2 = [ row[:] for row in board ]
vis = [[False]*N for _ in range(N)]
dir = [ [0,1], [0,-1], [1,0], [-1,0] ]
ans = [0, 0]

def BFS (i, j, arr) : 
  q = deque() 
  q.append([i , j, arr[i][j]])
  vis[i][j] = True 
  while q : 
    curR, curC, curColor = q.popleft() 
    for r, c in dir :
      nxtR = curR + r 
      nxtC = curC + c 
      if nxtR < 0 or nxtC < 0 or nxtR >= N or nxtC >= N  or vis[nxtR][nxtC] : continue 
      if curColor == arr[nxtR][nxtC] : 
        vis[nxtR][nxtC] = True 
        q.append([ nxtR, nxtC, arr[nxtR][nxtC] ])
  return 1 


for i in range(N) : 
  for j in range(N) :
    if board[i][j] == 'G' : board2[i][j] = 'R' 
    if vis[i][j] : continue 
    ans[0] += BFS(i,j, board)  

vis = [[False]*N for _ in range(N)]
for a in range(N) : 
  for b in range(N) : 
    if vis[a][b] : continue 
    ans[1] += BFS(a,b, board2)  

print(*ans)
