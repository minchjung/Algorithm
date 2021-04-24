from collections import deque 
n, m  = map(int, input().split())
board = []
vis = [ [0]*m for _ in range(n) ]

for i in range(n):
    board.append(list(map(int, input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
picNum=0
maxArea =0 
for i in range(n): 
    for j in range(m): 
            if vis[i][j]==0 and board[i][j]==1 : 
                picNum+=1
                q = deque() 
                q.append((i,j))
                vis[i][j]=1
                area = 0 
                while q : 
                    area +=1
                    now = q.pop() 
                    for k in range(4):
                        nx = now[0] + dx[k] 
                        ny = now[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] ==1 and vis[nx][ny] ==0 : 
                            q.append((nx,ny))
                            vis[nx][ny] = 1 
                maxArea = max(maxArea, area)
print(picNum, maxArea, sep='\n')
