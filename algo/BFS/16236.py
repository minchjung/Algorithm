import heapq 
from collections import deque

N = int(input().strip())
board = [list(map(int, input().strip().split())) for _ in range(N)]
fishes = [] # size, row, col
dx = [1,-1,0,0]
dy = [0,0,-1,1]
shark = []

def fishSearch (sharkSize) : 
  global fishes, shark 
  fishes = []
  for i in range(N):
    for j in range(N) :
      if not board[i][j] : continue  
      if board[i][j] == 9 : shark = [sharkSize, i, j]
      elif board[i][j] < sharkSize : fishes.append([board[i][j], i, j])

def BFS(ori, target): 
  #  ori = [size, r, c]  target = [fish-size, r, c]
  Q = deque()
  vis = [ [False]*N for _ in range(N) ]
  Q.append([0,ori[1], ori[2]])
  vis[ori[1]][ori[2]] = True 

  while Q : 
    t, r, c = Q.popleft() 
    if r == target[1] and c == target[2] : 
      return [t, r, c]
    for d in range(4) : 
      nr, nc = r + dx[d], c + dy[d]
      if nr >= N or nc >= N or nr < 0 or nc < 0 : continue 
      if vis[nr][nc] or board[nr][nc] > ori[0] : continue 
      vis[nr][nc] = True 
      Q.append([t+1,nr,nc])
  return [False, r, c]

curCnt = 0; totTime = 0;
fishSearch(2)
while fishes :
  d =[];
  for f in fishes :
    bfs = BFS(shark, f) 
    if not bfs[0] : continue  
    heapq.heappush(d, bfs)
  if not d : break 

  d.sort()
  a,b,c = heapq.heappop(d)
  board[shark[1]][shark[2]] = 0
  board[b][c] = 9 
  curCnt += 1; totTime += a
  
  if curCnt >= shark[0] : 
    curCnt = 0 
    shark[0]+=1
  fishSearch(shark[0])

print(totTime)