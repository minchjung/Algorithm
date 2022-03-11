# 1103 G2 게임
N, M = list(map(int, input().split()))
board = [ list(input()) for _ in range(N) ]
vis = [ [False]*M for _ in range(N) ]
dp = [ [-1]*M for _ in range(N) ]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
infcycle = False # 무한 사이클 체크용 

def DFS(r,c):
  global infcycle
  if infcycle : print(-1); quit() # 답출력후 프로그램 종료 (재귀를 아예 끝기위함)
  if dp[r][c] == -1 : 
    dp[r][c] = 1
    tem = 0 
    for d in range(4) : 
      nr, nc = r + dx[d]*int(board[r][c]), c + dy[d]*int(board[r][c])
      if nr >= N or nc >= M or nr < 0 or nc < 0 : continue  
      if board[nr][nc] =='H' : continue 
      if vis[nr][nc] : infcycle = True 
      vis[nr][nc] = True
      tem = max(tem, DFS(nr,nc))
      vis[nr][nc] = False 
      # vis back Tracking (그들만의 vis 영역으로 다시 재 방문을 체크하고 빠져 나오면 다시 Back돌려준다)
    dp[r][c] += tem 

  return dp[r][c]

vis[0][0] = True
DFS(0,0)
print(dp[0][0])