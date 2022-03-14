from collections import deque
# 2486 BFS 안전 영역
#  entry point 대한 고민
N = int(input())
board = [ list(map(int, input().strip().split())) for _ in range(N) ]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

entry = []
for i in range(N) : 
  for j in range(N) :
    if board[i][j] in entry : continue 
    entry.append(board[i][j])
ans = 0
for h in entry : 
  vis = [[False]*N for _ in range(N)]
  cnt = 0 
  Q = deque()
 
  for x in range(N) :
    for y in range(N) :
      if h >= board[x][y] : continue
      if vis[x][y] : continue  
      Q.append([h, x, y])
      vis[x][y] = True 
      while Q : 
        h, r, c = Q.popleft()
        for d in range(4) : 
          nr, nc = r+dx[d], c+dy[d] 
          if nr >= N or nc >= N or nr < 0 or nc < 0 : continue 
          if vis[nr][nc] or board[nr][nc] <= h: continue  
          vis[nr][nc] = True 
          Q.append([h, nr,nc])
      cnt+=1
    ans = max(ans, cnt)
print(1 if not ans else ans)