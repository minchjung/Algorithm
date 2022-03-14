# 최대힙 
# py 특징 -마이너스로 구현
import heapq, sys
N = int(input())
q = []
for _ in range(N) : 
  n = int(sys.stdin.readline().rstrip());
  if n : heapq.heappush(q, -n) 
  else :
    if q : print(-heapq.heappop(q))
    else : print(0)