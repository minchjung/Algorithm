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

# Check col 
def colCheck(col, number)  :
  for i in range(9) :
    if board[i][col] == number :return False; 
  return True; 

# Check 3x3
def crossCheck(x,y,number) : 
  startX = (x//3)*3
  startY = (y//3)*3
  for i in range(startX, startX+3) : 
    for j in range(startY, startY+3) : 
      if board[i][j] == number : return False; 
  return True; 

# BackTracking
def BackTracking  (k) :
  # break condtion 
  global done, ans; 
  if done : return 
  if k == len(stack) : # no blank => break 
    done = True;  # to stop the repeating return
    for i in range(9) : 
      print(*board[i]) # print Answer
    return 
  
  # process for recursion
  row, col = stack[k];
  for num in range(1,10) : 
    # check  row , col, 3x3  
    if num in board[row]  : continue; # row
    if colCheck(col,num) is False: continue; # col 
    if crossCheck(row, col, num) is False : continue; # 3x3 
    board[row][col] = num # put that value on the blank spot
    BackTracking(k+1) # recursive call same function for the next spot
    board[row][col] = 0 ; # back Track if it returns with no answer (no break condition)

BackTracking(0)
