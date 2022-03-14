# 1715 카드 정리
# https://www.acmicpc.net/problem/1715
import heapq 
N = int(input())
q = [ int(input()) for _ in range(N) ]
ans = 0 
heapq.heapify(q)
while len(q) > 1 : 
  sum = heapq.heappop(q) + heapq.heappop(q)
  ans+= sum
  heapq.heappush(q, sum)
print(ans)
