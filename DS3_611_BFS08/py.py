# 611<BFS>[S2]4963_py
from collections import deque 
n=1 
m=1
while n>0 or m>0 : 
    n,m =map(int, input().split())
    board = [ list(map(int, input().split())) for _ in range(m)]
    vis = [[0]*n for _ in range(m)]
    dX = [0, 0,-1, 1, 1, 1,-1,-1]
    dY = [1,-1, 0, 0, 1,-1, 1,-1]
    cnt = 0
    for i in range(m):
        for j in range(n): 
            if vis[i][j]==1 or board[i][j]==0 : continue 
            q = deque() 
            q.append([i,j])
            vis[i][j]=1
            cnt+=1
            while q : 
                now = q.popleft() 
                for d in range(len(dX)): 
                    nX = now[0]+dX[d]
                    nY = now[1]+dY[d]
                    if 0<=nX<m and 0<=nY<n and vis[nX][nY]==0 and board[nX][nY]==1: 
                        q.append([nX,nY])
                        vis[nX][nY]=1
    if n!=0 and m!=0 :print(cnt) 
    # 0 0 입력시 출력되게 했더니 틀렸다고 나옴..;;;