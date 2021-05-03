# 611<BFS>[S2]7562_py
from collections import deque 
T= int(input())
dX = [2, 2,-2,-2, 1, 1,-1,-1]
dY = [1,-1, 1,-1, 2,-2, 2,-2]
for _ in range(T):
    n = int(input())
    oi,oj=map(int, input().split())
    ti,tj=map(int, input().split())
    vis = [[0]*n for _ in range(n)]
    q = deque() 
    q.append([oi,oj])
    while q : 
        now = q.popleft() 
        if now==[ti,tj] : break 
        for i in range(len(dX)):
            nX = now[0] + dX[i]
            nY = now[1] + dY[i]
            if 0<=nX<n and 0<=nY<n and vis[nX][nY]==0: 
                vis[nX][nY]=vis[now[0]][now[1]]+1 #최단거리를 계속 memozation  
                q.append([nX,nY])
    print(vis[ti][tj])