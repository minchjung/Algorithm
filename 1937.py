# 1937 욕심쟁이 판다
from sys import setrecursionlimit 
setrecursionlimit(10**9)

N = int(input())
board = [ list(map(int, input().split())) for _ in range(N) ]
dp = [ [-1]*N for _ in range(N) ]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def DFS(r, c) : 
  if dp[r][c] != -1 : return dp[r][c]
  tem = 0 
  dp[r][c] = 1
  for d in range(4):
    nr, nc = r + dx[d], c + dy[d]
    if nr >= N or nc >= N or nr < 0 or nc < 0 : continue 
    if board[r][c] >= board[nr][nc] : continue 
    tem = max(tem, DFS(nr,nc))
  dp[r][c] += tem 
  return dp[r][c]
ans = 0
for r in range(N):
  for c in range(N):
    ans = max(ans,DFS(r,c))
print(ans)
