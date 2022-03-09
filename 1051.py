# 1051 숫자 정사각형 
# https://www.acmicpc.net/problem/1051
N, M = map(int, input().split());
board = [ list(map(int, list(input()))) for _ in range(N)]
ans = 0

for r in range(N) : 
  for c in range(M) : 
    for d in range(0, min(N,M)): 
      if r + d >= N or c + d >= M : continue 
      if board[r][c] == board[r+d][c] == board[r][c+d] == board[r+d][c+d] :
        ans = max(ans, d+1)

print(ans**2)