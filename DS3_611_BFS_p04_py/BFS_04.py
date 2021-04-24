from collections import deque 

dx = [0,0,-1,1]
dy = [-1,1,0,0]
def BFS(n,m,k):
    num =0
    board = [[0]*m for _ in range(n)] 
    vis  =  [[0]*m for _ in range(n)] 
    for i in range(k):
        b,a =map(int, input().split())
        board[a][b]=1 
    for i in range(n):
        for j in range(m):
            if board[i][j]!=1 or vis[i][j]!=0: continue
            num+=1
            q=deque();
            q.append([i,j])
            vis[i][j]=1
            while q: 
                now = q.pop() 
                for d in range(4):
                    nx = now[0] + dx[d]
                    ny = now[1] + dy[d]
                    if nx<0 or nx>=n or ny<0 or ny>=m: continue 
                    if board[nx][ny]==0 or vis[nx][ny]==1: continue 
                    q.append([nx,ny])
                    vis[nx][ny]=1
    return num 
t =int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    print( BFS(n,m,k) ) 