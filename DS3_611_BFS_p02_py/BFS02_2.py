# 611<BFS>[미로탐색]2178_p02_py
from collections import deque 
n,m =map(int, input().split())
board= [] 
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for i in range(n):
    board.append(list(map(int, list(input()))))

vis = [[-1]*m for _ in range(n)]
vis[0][0]=1
q = deque()
q.append([0,0])
while(q) :
    now = q.popleft()
    for k in range(4):
        nx = now[0] + dx[k]
        ny = now[1] + dy[k]
        if(0 > nx or nx >= n or 0 > ny or ny >=m or board[nx][ny]==0 or vis[nx][ny]!=-1 ): continue
        q.append((nx,ny))
        vis[nx][ny] = vis[now[0]][now[1]]+1 
        print(vis)
print(vis[-1][-1])
