# 1766 문제집:  위상정렬 2h
# https://www.acmicpc.net/problem/1766
# 힙 연습 하다가 위상정렬 까지 오게 됨
# 선수과목, 선수간선, 먼저 지나쳐야할 길 존재시 
# 먼저 지나칠게 하나 없는 정보를 두고 (indg=0) 활용하는 위상정렬을 
# 우선선위 큐 (힙)과 같이 사용하여서 BFS형태로 구현 
# 
# 1. 우선순위가 필요한 간선 정보는 그만큼 indg++ 
# 2. indg =0 , 우선으로 갈 필요없는 간선 부터 우선순위 큐에 (또다른 우선순위가 있다면 큐로직에 추가해 넣어줌) 
# 3. BFS pop 하면서 ans추가 
# 4. 연결 간선 탐색 = 연결 간선 -1 ,indg = 0이면 Q push, 
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

# 6 7
# 5 6
# 5 2
# 2 4
# 4 3
# 2 1
# 6 1
# 1 3

# 6 7
# 5 6
# 5 2
# 2 4
# 4 3
# 2 1
# 6 1
# 1 3
# ans: 5 2 4 6 1 3
# output 5 2 6 1 4 3