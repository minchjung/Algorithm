# 최소힙 구현 s2 
# 그냥 heapq 
#  출력 하나 아래다 더하고 있는 이상한짓으로 wrong
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