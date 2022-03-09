# 최소힙 구현 s2 
import heapq, sys

N = int(input())
q = [] 
for _ in range(N) :
  n =int(sys.stdin.readline())
  if n == 0 : 
    if not q : print(0)
    else : print(heapq.heappop(q))
  else : 
    heapq.heappush(q, n)