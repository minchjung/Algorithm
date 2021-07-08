from collections import deque
from itertools import permutations

n = int(input())
scv = list(map(int, input().split()))
for _ in range(3 - n) : scv.append(0)
Q = deque([(scv, 0)]) 
memo = [[[False]*61 for _ in range(61)] for _ in range(61)]
combin = list(permutations([9, 3, 1], 3))
  
def BFS():
  while(Q):
    scv, count = Q.popleft()
    a, b, c = scv
    if a == 0 and b == 0 and c == 0: return count
    if memo[a][b][c] is True: continue
    memo[a][b][c] = True
    for demage in combin:
      _a, _b, _c = max(0, a-demage[0]), max(0, b-demage[1]), max(0, c-demage[2])
      Q.append(([_a, _b, _c], count+1))
print(BFS())