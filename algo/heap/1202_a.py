#  보석도둑 
# 핵심은 둘다 무게가 작은걸로 비교 
# 가방에 작은 무게 부터 담을 수 있는 범위내의 보석을 모두 담는 것
# 그 다음 가방은 이미 앞에서 담은 무게보다 크기 때문에 다시 검색하지 않아도 됨
# 따로 그 다음 보석을 검색할 idx를 설정해두고 증가 시켜줌
# 전체 pq 주머니에 일단 담을 수 있는 보석을 다 담아두고 
# 하나씩 pop해서 최대 root 값만 가져 오는것  

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