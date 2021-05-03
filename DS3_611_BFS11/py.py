# 611<BFS>[S1]2667_py
from collections import deque 
N = int(input())
board=[]
vis=[[0]*N for _ in range(N)]
dX = [1,-1,0,0]
dY = [0,0,1,-1]
for _ in range(N):
    board.append(list(map(int, list(input()))))
ans = []
for i in range(N):
    for j in range(N): 
        if board[i][j]==0 or vis[i][j]!=0: continue 
        vis[i][j]=1;
        q = deque() 
        q.append([i,j])
        # 시작지점 부터  단지수를 초기화
        cnt=1 
        while q: 
            now = q.popleft()
            for d in range(len(dX)):
                nX = now[0]+dX[d]
                nY = now[1]+dY[d]
                if 0<=nX<N and 0<=nY<N and vis[nX][nY]==0 and board[nX][nY]==1:
                    # 연결되고 범위내이며 갈수있으며, 아직 안간곳을 모두 카운트 후 방문처리,queu push
                    cnt+=1
                    vis[nX][nY]=1
                    q.append([nX,nY])
        # 시작부터 BFS모두 탐색된 cnt 메모를 또 추가로 ans에 메모제이션한다. 
        ans.append(cnt)
# 길이가 총단지 수 
print(len(ans)) 
ans.sort()
for a in ans:
    print(a) 
    # 기록된 값을 오름차순으로 출력 