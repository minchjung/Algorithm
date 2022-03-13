from collections import deque
# 2206
N, M = map(int, input().strip().split())
board = [ list(map(int,list(input().strip()))) for _ in range(N) ]
dx = [0,0,1,-1]
dy = [-1,1,0,0]
INF = N*M+100

ans = INF
vis = [ [[False, False] for _  in range(M)] for a in range(N) ]
Q = deque([[-1,1,0,0]])
vis[0][0][0] = True 
vis[0][0][1] = True
dist = 0 
while Q : 
  t, p, r, c = Q.popleft()
  if r == N -1 and c == M -1 : 
    dist = t
    break 
  for d in range(4) : 
    nr, nc = r + dx[d], c + dy[d]
    if nr >= N or nc >= M or nr < 0 or nc < 0 : continue 
    if p : 
      if not vis[nr][nc][0] : 
        if not board[nr][nc] : 
          vis[nr][nc][0] = True
          Q.append([t-1, p, nr, nc]) 
        else : 
          vis[nr][nc][1] = True 
          Q.append([t-1, 0, nr, nc])
    else : 
      if not vis[nr][nc][1] and not board[nr][nc] : 
        vis[nr][nc][1] = True
        Q.append([t-1, 0, nr, nc]) 

ans = min(ans, -dist if dist else INF) 
print(-1 if ans == INF else ans)