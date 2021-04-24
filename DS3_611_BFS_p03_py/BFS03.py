# DS3_611_BFS[토마토]7576p03_py
from collections import deque 
m, n= map(int, input().split())
board = []
vis = []
dx = [0,0,-1,1]
dy = [-1,1,0,0] 
for _ in range(n):
    board.append(list(map(int,input().split())))
    vis.append([0]*m)
# Q initialize 
q = deque();
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 :
            q.append([i, j])
        if board[i][j] == 0 : 
            vis[i][j] = -1
# vis -1 : only place that bfs should go search
# vis 0 : nothing but initial number
# vis 1,2,3,4 .. : distance or the day count from the start point
while q  : 
    now = q.popleft()
    for d in range(4):
        nx = now[0]+ dx[d]
        ny = now[1]+ dy[d]
        # if next direction not in the range of board map, go to check the start of while loop
        if nx < 0 or nx >= n or ny < 0 or ny >= m : continue  
        # if next direction in the range, but already visited(vis =1,2,3...) 
        # or no place(vis=0) to search  (which is visit not -1), go to check the start of while loop
        if vis[nx][ny] !=-1 : continue 
        # you can visit within the range of board, than go increase the visit number +1 from the previous one
        # and put it in the q 
        vis[nx][ny]=vis[now[0]][now[1]]+1;
        q.append([nx,ny])
ans=0;
check = True 
#  check there is visit= -1 (means still left over fresh tomato and not reachable) 
for i in range(n):
    for j in range(m):
        ans=max(ans,vis[i][j])
        if vis[i][j]==-1 :
            check =False
if check: print(ans)
else: print(-1)