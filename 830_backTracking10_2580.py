# global 
board = [] 
stack = [] ;
done = False;
ans = [] 

# input 
board = [ list(map( int, input().split(" "))) for i in range(9)]

# get [col,row] coordinates for 0 (blank) on the board
for i in range(9) :
  for j in range(9) :
    if board[i][j] == 0 : stack.append([i,j])

# 가로, 세로 중복 검사
def colCheck(col, number)  :
  for i in range(9) :
    if board[i][col] == number :return False; 
  return True; 

# 3x3 중복 검사
def crossCheck(x,y,number) : 
  startX = (x//3)*3
  startY = (y//3)*3
  for i in range(startX, startX+3) : 
    for j in range(startY, startY+3) : 
      if board[i][j] == number : return False; 
  return True; 

# DFS
def DFS  (k) :
  # break condtion 
  global done, ans;  
  if done : return 
  if k == len(stack) : # no blank => break 
    done = True;  # to stop the repeating return
    for i in range(9) : 
      print(*board[i])
    return 
  
  # process for recursion
  row, col = stack[k];
  for num in range(1,10) : 
    # check  가로 , 세로, 3x3  
    if colCheck(col,num) is False: continue; 
    if crossCheck(row, col, num) is False : continue; 
    if num in board[row]  : continue;
    board[row][col] = num
    DFS(k+1)
    board[row][col] = 0 ; 

DFS(0)
