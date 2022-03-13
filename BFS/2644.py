# 2644 촌수계산 , S2
from collections import deque 
N = int(input())
f, t = map(int, input().strip().split())
board = [[] for _ in range(N+1)]
vis = [False]*(N+1)

for _ in range(int(input().strip())):
  a, b = map(int, input().strip().split())
  board[a].append(b)
  board[b].append(a)

Q = deque([[0,f]])
vis[f] = True; ans = -1; 
while Q : 
  dis, cur = Q.popleft()
  if cur == t : ans = dis; break  
  for nxt in board[cur] : 
    if vis[nxt] : continue 
    vis[nxt] = True 
    Q.append([dis+1, nxt])
print(ans)
