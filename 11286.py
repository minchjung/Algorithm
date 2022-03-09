# 절대값 힙 
import heapq, sys
N = int(sys.stdin.readline().rstrip())
q = []

for _ in range(N) : 
  n = int(sys.stdin.readline().rstrip())
  if n : 
    factor = -1 if n < 0 else 1 
    heapq.heappush(q, (n*factor,factor))
  else : 
    if q :
      a,b = heapq.heappop(q)
      print(a*b)
    else : print(0)    
