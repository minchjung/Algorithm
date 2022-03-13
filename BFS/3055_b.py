# 3055 탈출 G4 
# 물 BFS, 최단거리 BFS 
# 맵을 계속 갱신했지만, 비효율! 
from collections import deque

R, C = map(int, input().strip().split())
board = [ list(input()) for _ in range(R) ]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
water = []; start =[]; dest = [];

for i in range(R) : 
  for j in range(C) : 
    a = board[i][j] 
    if a == 'S' : start = [0,i,j]
    elif a == 'D' : dest = [i,j]
    elif a == '*' : water.append([i,j])

visB = [ [False]*C for _ in range(R) ]
sQ = deque([start])
INF = 10e11
ans = INF
visB[start[1]][start[2]] = True 
ori = [ b[:] for b in board ]

while sQ : 
  dist, r, c = sQ.popleft()
  if r == dest[0] and c == dest[1] : 
    ans = min(ans, dist); break 
  circle = dist+1 
  ref = [ b[:] for b in board ]

  while circle :
    circle -=1  
    for i in range(R) : 
      for j in range(C) :
        if board[i][j] != '*' : continue  
        for k in range(4): 
          wr, wc = i + dx[k], j + dy[k]
          if wr >= R or wc >= C or wr < 0 or wc < 0 : continue 
          if board[wr][wc] == 'X' or board[wr][wc] == 'D' or board[wr][wc] == '*': continue 
          ref[wr][wc] = '*'
    board = [ r[:] for r in ref ]

  for d in range(4) : 
    nr, nc = r + dx[d], c + dy[d] 
    if nr >= R or nc >= C or nr < 0 or nc < 0 : continue 
    if visB[nr][nc] or ref[nr][nc] == '*' or ref[nr][nc] == 'X' : continue 
    visB[nr][nc] = True 
    sQ.append([dist+1, nr, nc])
  board = [ o[:] for o in ori]

print('KAKTUS' if ans == INF else ans )