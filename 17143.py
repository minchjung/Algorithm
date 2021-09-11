R, C, M = map(int, input().split()) 
board = [ [0]*C  for _ in range(R)]
for _ in range(M) : 
  r, c, s, d, z = map(int, input().split())
  board[r-1][c-1] = [s, d, z]

hunt = [b[:] for b in board] # Use this array after hunting
move = [[0]*C for _ in range(R)] # mark for shark on the spot 
ans = 0 

# first process of each sec
def hunting(col) : 
  # col => hunter's col 
  global ans, board;
  for r in range(R) : 
    if board[r][col] != 0 : # find out it at the lowest row
      ans += board[r][col][2] # add that size  
      board[r][col] = 0 # update the orinal board arr
      return
# second process of each sec
def moving(r,c,s,d,z) : 
  global R, C
  x = 0; sub = 0; 
  tot = s; end = 0; 
  isX_row = True; 
  
  # assign the value for moving back and forth
  if d == 1 : # upward : x=row => row-1 
    x = r; sub = -1; end = R 
  elif d == 2 : # downward : x=row => row +1 
    x = r; sub = 1; end = R  
  elif d == 3 : # forward(right) : x=col => col +1 
    x = c; sub = 1; end = C 
    isX_row = False  
  else : # backward(left) : x=col => col -1
    x = c; sub = -1; end = C 
    isX_row = False

  # count when it converts its direction
  cnt = 0 
  while tot : 
    if tot != 0 and x + sub < 0 : # this!! needs to debug
      sub *= -1; cnt += 1 
    if tot != 0 and x + sub > end -1 : 
      sub *= -1; cnt += 1
    x += sub  
    tot -= 1
  
  # if its odd => direction's been changed
  if cnt % 2 : 
    if d == 1 : d = 2
    elif d == 2 : d = 1
    elif d == 3 : d  = 4 
    else : d = 3

  # set the shark on new spot with new direction(or not)
  if isX_row : # x was intially marked if its row or not 
    if move[x][c] == 0 : # first to check the move array!!
      hunt[x][c] = [s, d, z] # since it contains 0 or 1 
      move[x][c] = 1  # 0 means no one's ever spotted ,so take that on and mark it as spotted =1
    elif hunt[x][c][2] < z : # 1 => if there's one on that place,
      hunt[x][c] = [s, d, z] # compare the size, and replace if its possible
  else : # same thing  when x= colum
    if move[r][x] == 0 : 
      hunt[r][x] = [s, d, z]
      move[r][x] = 1 
    elif hunt[r][x][2] < z : 
      hunt[r][x] = [s, d, z]

for c in range(C): 
  hunting(c) # hunting first 
  move =[[0]*C for _ in range(R)] # initialize both move, hunt
  hunt =[[0]*C for _ in range(R)]
  for i in range(R) : 
    for j in range(C) : 
      # Use board (unchaged array on moving process) 
      # as to find the place of shark 
      if board[i][j] == 0 : continue  
      speed, direct, size = map(lambda x: x, board[i][j])
      moving(i, j, speed, direct, size)
  # After moving process, updated whole board array for next hunt 
  board = [ h[:] for h in hunt ]
print(ans)