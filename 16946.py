from collections import deque 

N, M = map(int, input().split())
board = [ list(map(int, input())) for _ in range(N) ]

vis = [ [False]*M for _ in range(N) ]
ans = [ m[:] for m in board ]
dir = [ [0,1],[0,-1],[1,0],[-1,0] ]

for r in range(N) : 
  for c in range(M) : 
    if not board[r][c] and not vis[r][c] : 
      q = deque()
      q.append([r,c])
      cnt = 1
      ones = [] 
      vis[r][c] = True
      
      while q : 
        curR, curC = q.popleft() 
        for x , y  in dir : 
          nxtR = curR + x
          nxtC = curC + y
          if nxtR < 0 or nxtC < 0 or nxtR >= N or nxtC >= M : continue 
          if vis[nxtR][nxtC] : continue 
          vis[nxtR][nxtC] = True 
          if not board[nxtR][nxtC] :
            cnt +=1 
            q.append([ nxtR, nxtC ])
          else : 
            ones.append([ nxtR, nxtC ])
      
      for nxtr, nxtc in ones :
        vis[nxtr][nxtc] = False 
        ans[nxtr][nxtc] += cnt 
        ans[nxtr][nxtc] %= 10 

for a in ans : print(''.join(map(str, a)))
