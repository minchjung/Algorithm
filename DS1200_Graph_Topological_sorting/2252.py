
from collections import deque 

N, M = map(int, input().split())
board = [ [] for _ in range(N+1)] 
indeg = [0]*(N+1)

for i in range(M): 
    a, b = map(int, input().split())
    board[a].append(b)
    indeg[b] += 1

Q = deque()
ans = []
for i in range(1,N+1):
    if indeg[i] ==0 : 
        Q.append(i)
while Q : 
    cur = Q.popleft()
    ans.append(cur)
    for nxt in board[cur] : 
        indeg[nxt] -=1 
        if indeg[nxt] == 0 : 
            Q.append(nxt)
print(*ans)