# 절대값 힙 
# https://www.acmicpc.net/problem/11286
#  힙 튜플로 두개 활용 
#  부호 같이 넣어줄때 챙겨주기
#  힙은 앞에 첫번째 원소로만 적용 

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
