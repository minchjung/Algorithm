#  장난감 조립
import heapq, sys 

N = int(sys.stdin.readline().strip());
M = int(sys.stdin.readline().strip());

graph = [[] for _ in range(N+1)]
board = [[0]*(N+1) for _ in range(N+1)]
indg = [0]*(N+1) 
ans = indg[:] 

for _ in range(M):
  a,b,c = map(int, sys.stdin.readline().strip().split())
  graph[a].append(b)
  board[a][b] = c 
  indg[b]+=1 

pq = [] 
for i in range(1,N+1) :
  if indg[i] == 0 : 
    heapq.heappush(pq, i)
    ans[i] = 1
while pq : 
  cur = heapq.heappop(pq)
  for n in graph[cur] : 
    indg[n] -= 1 
    ans[n] += ans[cur]*board[cur][n]
    if not indg[n] : 
      heapq.heappush(pq, n)

for i in range(1, N+1): 
  if not graph[i] : print(i, ans[i])