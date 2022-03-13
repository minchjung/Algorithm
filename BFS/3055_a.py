# 3055 탈출 G4 
# 물 BFS, 최단거리 BFS 
from collections import deque

R, C = map(int, input().strip().split())
board = [ list(input()) for _ in range(R) ]

waterDay = [ [0]*C for _ in range(R) ]
visW = [ [False]*C for _ in range(R) ]
visB = [ [False]*C for _ in range(R) ]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
INF = 10e11; ans = INF
water = []; start =[]; dest = [];

for i in range(R) : 
  for j in range(C) : 
    a = board[i][j] 
    if a == 'S' : start = [0,i,j]
    elif a == 'D' : dest = [i,j]
    elif a == '*' : 
      water.append([0,i,j])
      visW[i][j] = True 
# BFS water speard 시간 지도
wQ = deque(water)
while wQ : 
  t, x, y = wQ.popleft()
  for d in range(4) : 
    nx, ny = x + dx[d], y + dy[d]
    if nx >= R or ny >= C or nx < 0 or ny < 0 : continue 
    if visW[nx][ny] or board[nx][ny] == 'X' or board[nx][ny] == 'D' : continue 
    visW[nx][ny] = True 
    waterDay[nx][ny] = t + 1
    wQ.append([t+1, nx, ny])

# BFS 최단거리  (board 장애물, vis, water speard 까지 추가로 참조!)
sQ = deque([start])
visB[start[1]][start[2]] = True 
while sQ : 
  dist, r, c = sQ.popleft()
  if r == dest[0] and c == dest[1] : 
    ans = min(ans, dist); break 
  for d in range(4) : 
    nt, nr, nc = dist + 1,r + dx[d], c + dy[d] 
    if nr >= R or nc >= C or nr < 0 or nc < 0 : continue 
    if visB[nr][nc] or board[nr][nc] == '*' or board[nr][nc] == 'X' : continue
    if waterDay[nr][nc] and waterDay[nr][nc] <= nt : continue  # water speard 시간 지도를 참조하는 추가 코드!! 
    visB[nr][nc] = True 
    sQ.append([dist+1, nr, nc])

print('KAKTUS' if ans == INF else ans )
# 같이 spread! 하는 경우 BFS 2번인데 
# 시간의 동일성을 착안해서 !! 시간 지도맵, spread 지도를 만들어서 하나로 참조!! 하는 법!! 