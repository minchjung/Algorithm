# 1655 가운데를 말해봐요 
import heapq, sys 

N = int(sys.stdin.readline().rstrip())
lQ = []; rQ = []; 
for _ in range(N) :
  n = int(sys.stdin.readline().rstrip())
  if len(lQ) == len(rQ) : heapq.heappush(lQ, -n)
  else : heapq.heappush(rQ, n)
  if lQ and rQ and -lQ[0] > rQ[0] : 
    a = -heapq.heappop(lQ)
    b = heapq.heappop(rQ)
    heapq.heappush(lQ, -b)
    heapq.heappush(rQ, a)
  print(-lQ[0])
