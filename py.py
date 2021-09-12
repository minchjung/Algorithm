N, K = map(int, input().split())
# color info only
color = [list(map(int, input().split())) for _ in range(N)] 
# knight index start from 1 to K 
knight = [0]*(K+1) 
# board has knight index info only
board = [ [[0] for _ in range(N)] for _ in range(N) ] 
ans = 0 
done = False

for i in range(K) : 
  r, c, d = map(int, input().split())
  knight[i+1] =[r-1, c-1, d] 
  board[r-1][c-1] = [i+1]

def ODD (r,c,n,m): 
  return r < 0 or c < 0 or r >= n or c >= m   

def direction(curC, curR, curD ) : 
  if curD == 1 : curC += 1 ; 
  elif curD == 2 : curC -= 1 ; 
  elif curD ==3 : curR -= 1 ; 
  else: curR += 1; 
 
  return [curR, curC]

def reverseD(curD):
  if curD ==1 : return 2 
  elif curD == 2 : return 1 
  elif curD == 3 : return 4 
  return 3 

def onWhite(k, curR, curC, curD, nxtR, nxtC, isWhite):
  global ans, done
  tem = board[curR][curC][:]

  if isWhite is False: tem.reverse()
  if board[nxtR][nxtC][0] != 0 : # next position not empty
    newK = board[nxtR][nxtC][:] + tem[:] # [next things] + [cur things]
    board[nxtR][nxtC] = newK[:]
  else : board[nxtR][nxtC] = tem[:] # next empty => just set [cur things]

  for i in board[curR][curC] : 
    d = knight[i][2]
    knight[i] = [nxtR,nxtC,d]   
  # board[curC][curD] =[0][:] # Make the prev position empty

  ans = max( ans, len(board[nxtR][nxtC]) )   
  if ans >= 4 : done = True

T = 0
while T < 1001 :
  T += 1 
  if done : break
  for k in range(1, len(knight)) : 
    curR, curC, curD = knight[k]
    if board[curR][curC][0] != k : continue # board[r][c] = [knight1, knight2...]
    # if kinght1 is not on the bottom => continue (board[r][c] = [0] <- empty) 
    nxtR, nxtC = direction(curC, curR, curD) 
    falseCnt = 0 
    if ODD(nxtR, nxtC, N, N) :
      curD = reverseD(curD)
      nxtR, nxtC = direction(curC, curR, curD)
      if color[nxtR][nxtC] ==2 : 
        knight[k] = [curR,curC,curD]
        continue 
    elif color[nxtR][nxtC] == 0 : # white 
      onWhite(k, curR, curC, curD, nxtR, nxtC, True)
      board[curR][curC] = [0]
    elif color[nxtR][nxtC] == 1: # red 
      onWhite(k, curR, curC, curD, nxtR, nxtC, False)
      board[curR][curC] = [0]
    else : # blue
      blueD = reverseD(curD)
      blueR, blueC = direction(curC, curR, blueD)
      if ODD(blueR, blueC, N, N) or color[blueR][blueC] == 2: 
        knight[k] = [curR, curC, blueD]
        continue 
      if color[blueR][blueC] == 0 : 
        onWhite(k, curR, curC, blueD, blueR, blueC, True)
        board[curR][curC] = [0]
        knight[k] = [blueR, blueC, blueD]
      elif color[blueR][blueC] == 1 : 
        onWhite(k, curR, curC, blueD, blueR, blueC, False)
        board[curR][curC] = [0]
        knight[k] = [blueR, blueC, blueD]
    if done : 
      print(T)
      break
if T >= 1001 : print(-1)
