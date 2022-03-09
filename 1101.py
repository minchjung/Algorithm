# 1101 카드정리1
# https://www.acmicpc.net/problem/1101
N, M = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N) ]
ans = 1e10
for r in range(N): 
  card = [False]*M
  cnt = 0 
  for x in range(N) : 
    if r == x : continue 
    idx = board[x].index(max(board[x]))
    zero = board[x].count(0)
    if zero == M : continue 
    if M - zero == 1 and not card[idx]: 
      card[idx] = True 
      continue 
    cnt +=1 
  ans = min(ans, cnt)
print(ans)
