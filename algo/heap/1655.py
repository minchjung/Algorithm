# 1655 가운데를 말해봐요 
# 입력이 순차적으로 주어질때 가운데 수를 힙으로 !!
# 힙 2개 구현 
# 1,2,3,4,5,6,7  
#  ------왼쪽 최대힙 --- 오른쪽 최소힙------- 
# 왼쪽에서는 최대힙으로 구현한 root 값이 가운데 후보군 
# 오른쪽에서는 최소힙으로 구현한 root 값이 가운데 후보군 
# 두 heap의 길이가 같을경우 왼쪽 heap부터 채우고 
#  다르면 오른쪽 heap
#  왼쪽의 최대값 보다 오른쪽의 최소 값이 더 큰경우 
#  두 heap의 루트를 pop해서 교환해 준다 ! 
#  그러면 항상 가운데 값이 왼쪽 heap의 root로 뽑을 수 있다

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
