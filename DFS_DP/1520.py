#  1520 내리막길 g4
R, C = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(R) ]
vis = [ [-1]*C for _ in range(R) ]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def DFS(h,r,c):
  global cnt
  if r == R-1 and c == C-1 : return 1 
  if vis[r][c] != -1 : return vis[r][c] 
  vis[r][c] = 0
  for d in range(4): 
    nr, nc = r + dx[d], c + dy[d]
    if nr >= R or nc >= C or nr< 0 or nc < 0 : continue
    if board[nr][nc] >= h : continue 
    vis[r][c] += DFS(board[nr][nc], nr,nc)
 
  return vis[r][c]

DFS(board[0][0], 0,0)
print(vis[0][0])