# 1058 친구
# https://www.acmicpc.net/problem/1058
# 한다리 건너서만 친구 검사를 하면 된다 
# 즉 특정 조건 한번만 더 for 문을 돌리는 생각을 하자 
# vis 처리를 어디서 부터 해주는지 차이가 중요하다  
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

