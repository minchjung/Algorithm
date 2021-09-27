from collections import deque

def solution(maps):
    
    N = len(maps);M = len(maps[0])
    target = [N-1, M-1]
    INF = 1e9
    ans = INF

    vis = [[False]*M for _ in range(N)]
    dirX = [0,0,-1,1]
    dirY = [1,-1,0,0]

    q = deque([[0,0,1]])
    vis[0][0] = True
    while q : 
        row, col, dis = q.popleft()
        if row == target[0] and col == target[1] :
            ans = min(ans, dis)
        for i in range(4) :
            nxtR = row + dirX[i]; nxtC = col + dirY[i]
            if nxtR < 0 or nxtC < 0 or nxtR >= N or nxtC >= M : continue 
            if vis[nxtR][nxtC] : continue 
            if maps[nxtR][nxtC] == 0 : continue
            vis[nxtR][nxtC] = True 
            q.append([nxtR, nxtC, dis+1])

    return -1 if ans == INF else ans
a = solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])
print(a)