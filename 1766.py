import heapq
N, M = map(int, input().split())
board = [ [] for _ in range(N+1)]
indg = [0]*(N+1)
q = []

for _ in range(M) : 
  a, b = map(int, input().split())
  board[a].append(b)
  indg[b]+=1
for i in range(1, N+1):
  if not indg[i] : heapq.heappush(q, i)

ans = []
while q : 
  cur = heapq.heappop(q)
  ans.append(cur)
  for nxt in board[cur] : 
    indg[nxt]-=1
    if not indg[nxt] : heapq.heappush(q, nxt)
print(*ans)
