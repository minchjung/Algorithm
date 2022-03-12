# 2580 G4 스도쿠 
# 백트래킹 vis이 아닌 !! all 검사 후 = 원상복귀는 다시 빈 0값

sudoku = [ list(map(int, input().split())) for _ in range(9) ]
entry = [ ]
for i in range(9):
  for j in range(9): 
    if not sudoku[i][j] : entry.append([i,j])

def isNumOn3x3(x,y,num):
  for a in range(x-x%3, x-x%3+3):
    for b in range(y-y%3, y-y%3+3):
      if sudoku[a][b] == num : return True 
  return False 

def isNumOnRowAndCol(x,y,num): 
  if num in sudoku[x] : return True 
  for i in range(9):
    if sudoku[i][y] == num : return True 
  return False 

def DFS(cur):
  if cur == len(entry) :
    for i in range(9): print(*sudoku[i])
    quit()
  
  for n in range(1, 10):
    r, c = entry[cur][0], entry[cur][1] 
    if isNumOnRowAndCol(r,c,n) or isNumOn3x3(r,c,n) : continue 
    sudoku[r][c] = n
    DFS(cur+1)
    sudoku[r][c] = 0

DFS(0)