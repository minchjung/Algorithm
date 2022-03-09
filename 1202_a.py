
import heapq, sys
N, K = map(int, input().split())

dia = []; bag =[]  
for _ in range(N) : 
  w, v = map(int, sys.stdin.readline().rstrip().split())
  dia.append([w, -v])
for _ in range(K) :
  bag.append(int(sys.stdin.readline().rstrip())) 

ans = 0; idx = 0 
dia.sort(); bag.sort()
pq = [];
for i in range(K) : 
  while (N > idx and bag[i] >= dia[idx][0]) : 
    heapq.heappush(pq, dia[idx][1])
    idx+=1 
  if pq : ans -= heapq.heappop(pq)
print(ans)
# 2 2
# 5 5
# 5 5
# 1
# 10
# ans 5

# 4 2
# 4 100
# 5 110
# 6 90
# 7 80
# 5
# 7