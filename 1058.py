# 1058 친구
# https://www.acmicpc.net/problem/1058
 
N = int(input())
board = [ list(input()) for _ in range(N) ]
ans = 0 
for r in range(N) : 
  vis =[[False]*N for _ in range(N)]
  vis[r][r] = True 
  for c in range(N) : 
    if board[r][c] == 'N' : continue
    vis[r][c] = True 
    for d in range(N) : 
      if vis[r][d] or board[c][d] == 'N' : continue 
      vis[r][d] = True 
  ans = max(ans, vis[r].count(True))
print(ans-1)
