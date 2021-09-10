N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)] 

foods = [[5]*N for _ in range(N)]
board = [[ [] for _ in range(N) ] for _ in range(N)]

dirX = [1,0,-1,0,1,1,-1,-1];
dirY = [0,1,0,-1,-1,1,-1,1];
for _ in range(M) :
  x,y,v = map(int, input().split())
  board[x-1][y-1].append(v)

ans = 0
while K > 0 : 
  K -=1 
  # Spring and Summer
  for i in range(N) : 
    for j in range(N) :
        # new array for tree on [i][j]
        tree = board[i][j][:]
        tree = sorted(tree) # sort arr for young to feed first 
        newTree = []
        dead = []
        for k in range(len(tree)) : 
          if foods[i][j] - tree[k] >= 0 : # aged tree in newTree arr
            newTree.append(tree[k]+1) 
            foods[i][j] = foods[i][j] - tree[k] # foods updated by feeding above
          else : dead.append(tree[k]//2) # dead tree in dead arr
        board[i][j] = newTree[:] # update aged tree(w/o old to dead) on the spot[i][j]
        foods[i][j]+= sum(dead) # update foods by adding the dead one 
  # Autumn - propagation
  for i in range(N) : 
    for j in range(N) :
      for propa in board[i][j] :
        if propa % 5 != 0 : continue 
        for d in range(8) : 
          nxtX = i + dirX[d] ; nxtY = j + dirY[d]
          if nxtX < 0 or nxtX >= N or nxtY < 0 or nxtY >= N : continue 
          board[nxtX][nxtY].append(1)

  # Winter - add foods by A 
  # & get answer if its the last year
  for x in range(N) : 
    for y in range(N) :
      foods[x][y] += A[x][y]
      if K == 0 : ans += len(board[x][y]) 
print(ans)