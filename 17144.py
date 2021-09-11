R, C, T = map(int, input().split())
board = [ list(map(int, input().split())) for i in range(R) ]
cleaner = {'top': [0,0], "bottom": [0,0]}

dirX = [0,0,1,-1]
dirY = [1,-1,0,0] 

for i in range(R) : 
  for j in range(C) :
    if board[i][j] == -1 : cleaner['bottom'] = [i,j]
cleaner['top'] = [cleaner['bottom'][0] -1, cleaner['bottom'][1]]

while T : 
  T -= 1 
  ref = [ [0]*C for b in range(R)] # initiate ref array for every sec
  ref[cleaner['top'][0]][cleaner['top'][1]] = -1 
  ref[cleaner['bottom'][0]][cleaner['bottom'][1]] = -1 

  # diffuse
  for x in range(R) : 
    for y in range(C) : 
      if board[x][y] == 0 or board[x][y] == -1 : continue
      # find dust => firgue out to diffuse in 4 direction
      dirCnt = 0 ; 
      for d in range(4): 
        nxtX = x + dirX[d]; nxtY = y + dirY[d] 
        if nxtX < 0 or nxtX >= R or nxtY < 0 or nxtY >= C : continue 
        if board[nxtX][nxtY] == -1 : continue
        val = board[x][y] // 5 # value to diffuse (must set before)
        dirCnt += 1  # count if it diffuse
        ref[nxtX][nxtY] += val # set the value on diffused spot
      ref[x][y] += board[x][y] -val*dirCnt  # after 4 direction search, set value on origin 

  # Cleaner On  
  board = [r[:] for r in ref] 
  for nx in range(R) :# this going to be hell... 
    for ny in range(C) :
      if 0 <= nx <= cleaner['top'][0] : # upper part 
        if nx == cleaner['top'][0] and 0 < ny < C-1 : 
          ref[nx][ny+1] = board[nx][ny]  # upper-bottom line  => shift to col +1 (right)
          if ny == 1 : ref[nx][ny] = 0 
        elif 0 < nx <= cleaner['top'][0] and ny == C-1 : ref[nx-1][ny] = board[nx][ny] # right end col => shif to row -1 (up)
        elif nx == 0 and 0 < ny <= C-1 : ref[nx][ny-1] = board[nx][ny] # top-line => shift to col -1 (left)
        elif 0 <= nx < cleaner['top'][0] and ny == 0: # left end col => shift to row +1 (down) 
          if board[nx+1][ny] == -1  : ref[nx+1][ny] = -1
          else : ref[nx+1][ny] = board[nx][ny] # must not be on clearner spot
      elif cleaner['bottom'][0] <= nx < R: 
        if nx == cleaner['bottom'][0] and 0 < ny < C -1 : 
          ref[nx][ny+1] = board[nx][ny] # top line => shift to right : col + 1 
          if ny == 1 : ref[nx][ny] = 0
        elif cleaner['bottom'][0] <= nx < R -1 and ny == C -1 : ref[nx+1][ny]  = board[nx][ny] # right end ==> shift to down : row + 1
        elif nx == R -1 and 0 < ny <= C-1 : ref[nx][ny-1] = board[nx][ny] # bottom line ==> shift to left : col -1  
        elif cleaner['bottom'][0] < nx <= R -1 and  ny == 0 :
          if board[nx-1][ny] == -1 : ref[nx-1][ny] = -1
          else : ref[nx-1][ny] = board[nx][ny] # left end => shift to up : row - 1 
  board = [r[:] for r in ref] # replace array 

ans = 0 
for resDust in board : 
  for d in resDust : 
    if d > 0 : ans += d 
print(ans)