# 이중우선순위q
import heapq
T = int(input().strip())
for _ in range(T) :
  K = int(input())
  minQ =[]; maxQ = []
  vis = [False]*(K+1) 
  for i in range(K) :
    o, n = input().strip().split()
    if o == 'I' : 
      heapq.heappush(minQ, (int(n),i))
      heapq.heappush(maxQ, (-int(n),i))
      vis[i] =True
    else : 
      if n == '-1':
        while minQ and not vis[minQ[0][1]] : heapq.heappop(minQ)
        if minQ : 
          vis[minQ[0][1]] = False 
          heapq.heappop(minQ)
      else :
        while maxQ and not vis[maxQ[0][1]] : heapq.heappop(maxQ)
        if maxQ : 
          vis[maxQ[0][1]] = False 
          heapq.heappop(maxQ)

  while minQ and not vis[minQ[0][1]] : heapq.heappop(minQ)
  while maxQ and not vis[maxQ[0][1]] : heapq.heappop(maxQ)
  ans = [ -maxQ[0][0], minQ[0][0]] if maxQ and minQ else ['EMPTY'] 
  print(*ans)