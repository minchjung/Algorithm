#  저울 
# https://www.acmicpc.net/problem/2437
# import heapq
#  heappify 사용할때만 즉각즉각 써야함 ! 
#  리스트 한번에 정렬된 상태로 사용하려면 sort!!
#  a = a.sort() <- none Type 
#  a.sort() 
#  그다음 a가정렬됨 

# [1,2,3,4] 
# 표현할수 없는 최소 수 = 
# 1+2 해서 누적 sum으로 비교
#  sum 보다 다음수가 크면 sum보다 1큰 수가 표현 안되는 최소 수 
#  sum 이니셜 값 = 1 로 
N = int(input())
W = list(map(int,input().split()))
W.sort()
sum = 1;

for w in W : 
  if w > sum : break 
  sum += w
print(sum)