# 1325 효율적인 해킹 S1
# 시간초과 엣지 케이스!
#  힙 자료형 10분 활용 그리고 
#  조건을 또 한번 정확하게 분리해야 !! 한다!! 
#  특히 답 도출 구역에서는 조건하나를 허술하게 구현하면 엣지 케이스 바로 걸리며 고생할 수 있따   
import heapq
N ,M = map(int, input().strip().split())
board = [ [] for _ in range(N+1) ]

for _ in range(M):
  a, b = map(int, input().strip().split())
  board[b].append(a)

ans = [0]*(N+1)
pq = []
# DFS
for i in range(1,N+1) : 
  vis = [False]*(N+1) 
  stack = [i]
  vis[i] = True; 
  while stack : 
    cur = stack.pop() 
    for nxt in board[cur] : 
      if vis[nxt] : continue 
      vis[nxt] = True 
      stack.append(nxt)
      ans[i] += 1
  # 답도출 위한 (시간 초과 해결) 힙 자료형 
  if not pq : heapq.heappush(pq, (-ans[i], i)) 
  else :  #분기를 정확하게 딱딱 나눠야지 엣지에 하나도 안걸림 
    if -pq[0][0] > ans[i] : continue 
    if -pq[0][0] == ans[i] : heapq.heappush(pq, (-ans[i], i))
    else : 
      while pq : heapq.heappop(pq)
      heapq.heappush(pq, (-ans[i],i))
while pq : 
  print(pq[0][1])
  heapq.heappop(pq)