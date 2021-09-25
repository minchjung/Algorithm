from collections import deque
from itertools import combinations

N, M  = map(int, input().split())
board = [ [0]*N  for _ in range(N)]
dirX = [0,0,-1,1]
dirY = [1,-1,0,0]
virSpot = []
for i in range(N):
    for j, num in  enumerate( list( map(int, input().split()) ) ):
        if num == 2 : 
            virSpot.append([i,j, 0])
        board[i][j] = num

minAns = N*N*N 
for comb in combinations( virSpot, M) : 
    q = deque()
    vis = [[False]*N for _ in range(N)]
    ref = [[0]*N for _ in range(N)]
    maxTime = 0 

    for com in comb :q.append(com)
    for i in range(N):
        for j in range(N) :
            if board[i][j] == 1 : vis[i][j] = True
    while q : 
        row, col, sec = map(int, q.popleft())
        vis[row][col] = True
        for d in range(4) :
            nxtRow = dirX[d] + row; 
            nxtCol = dirY[d] + col
            if nxtRow < 0 or nxtCol < 0 or nxtRow >= N or nxtCol >= N : continue 
            if vis[nxtRow][nxtCol] : continue  
            ref[nxtRow][nxtCol] = sec +1
            vis[nxtRow][nxtCol] = True 
            q.append([nxtRow, nxtCol, sec+1])
    
    boolCheck = True 
    for v in vis :
        if False in v :
            boolCheck = False 
            break 
    if boolCheck : 
        for i in range(N) :
            for j in range(N) :
                if board[i][j] == 0 :
                    maxTime = max(maxTime, ref[i][j])
        minAns = min(minAns, maxTime)
if minAns == N*N*N : print(-1)
else : print(minAns)