# 611<BFS>[S2]11724_py
from collections import deque 
N,M = map(int, input().split())
board =[[]for _ in range(N+1)]
board[0].append(0)
vis=[0]*(N+1)
for _ in range(M):
    a,b=map(int, input().split())
    board[a].append(b)
    board[b].append(a)

cnt=0
for i in range(1,N+1):
    if vis[i]!=0: continue
    q = deque() 
    q.append(board[i])
    vis[i]=1
    cnt+=1
    while q : 
        now = q.popleft() 
        for a in now :
            if vis[a]!=0: continue  
            vis[a]=1
            q.append(board[a])
print(cnt)

