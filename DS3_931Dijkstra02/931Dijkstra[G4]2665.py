# 931Dijkstra[G4]2665
import heapq 
N = int(input())
board = [list(map(int,list(input()))) for _ in range(N)]
vis= [[-1]*N for _ in range(N)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]

hp = [[0,(0,0)]] 
heapq.heapify(hp)
vis[0][0]=0
while hp: 
    now = heapq.heappop(hp)
    x=now[1][0]
    y=now[1][1]
    for i in range(4): 
        nx = x + dx[i] 
        ny = y + dy[i] 
        if nx < 0 or nx >= N or ny < 0 or ny >= N or vis[nx][ny]!=-1: continue 
        if board[nx][ny]==0 : vis[nx][ny] = vis[x][y]+1    
        else: vis[nx][ny]=vis[x][y]
        heapq.heappush(hp, [vis[nx][ny], (nx,ny)])
print(vis[N-1][N-1])