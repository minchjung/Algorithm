# 611<BFS>[S1]영역구하기2583_py
from collections import deque 
M,N,K = map(int, input().split())
board=[[0]*(N) for _ in range(M)]
vis=[[0]*(N) for _ in range(M)]
dX = [1,-1,0,0]
dY = [0,0,1,-1]
for _ in range(K):
    # 아래가 0,0인 좌표값들 보정 and 눈금이 아니라 칸 자체가 좌표가 되게 보정 
    bC,bR,tC,tR=map(int, input().split())
    bR = M-bR -1
    tR = M-tR 
    tC -=1
    for i in range(tR,bR+1): 
        for j in range(bC,tC+1):
            board[i][j]=1
# BFS 매 탐색마다 연결되는 node 수들을 저장
ans=[]
for i in range(M):
    for j in range(N): 
        if vis[i][j]==1 or board[i][j]==1: continue 
        vis[i][j]=1
        # 최초 시작 node부터 count 초기화
        cnt=1
        q=deque()
        q.append([i,j])
        # 1개의 시작노드 부터 BFS 
        while q: 
            now = q.popleft()
            for d in range(len(dX)):
                nX = now[0]+dX[d]
                nY = now[1]+dY[d]
                if 0<=nX<M and 0<=nY<N and vis[nX][nY]==0 and board[nX][nY]==0:
                    vis[nX][nY]=1 
                    cnt+=1 # 방문하지 않고 갈수있는 곳이며 연결된 node이므로 카운트해주고
                    q.append([nX,nY])
        ans.append(cnt)# BFS 탐색종료시 cnt를 저장 
ans.sort()
print(len(ans))
print(*ans)    
