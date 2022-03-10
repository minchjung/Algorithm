from collections import deque
import heapq

N, M = map(int, input().strip().split()) 
board = [ [] for _ in range(N+1) ]

for _ in range(M) : 
  a, b =map(int, input().strip().split())  
  board[a].append(b)
  board[b].append(a)
  
minAns =[] 
heapq.heappush(minAns, (N**N,1))
for i in range(1, N+1) : 
  vis = [False]*(N+1)
  Q = deque([ [0,i] ])
  vis[i] = True 
  ans = [0]*(N+1)

  while Q : 
    dist, cur = Q.popleft()
    for nxt in board[cur] : 
      if vis[nxt] : continue 
      vis[nxt] = True
      ans[i] += dist + 1 
      Q.append([dist+1, nxt])
  if minAns[0][0] >= ans[i] : 
    heapq.heappush(minAns, (ans[i], i))

print(minAns[0][1])