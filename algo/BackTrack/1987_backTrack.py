# 1987 알파벳 G4 
R,C = map(int, input().split())
board = [ list(map(lambda x : ord(x) - ord('A'),list(input().strip()))) for _ in range(R) ]
vis = [ [False]*C for _ in range(R) ]
alph =[False]*26;

dx = [0,0,1,-1]; dy = [1,-1,0,0]
vis[0][0] = True; alph[board[0][0]] = True 
ans = 0;

def DFS(r,c, tot):
  global ans
  done = False  # check! if there's no where to go  
  
  for d in range(4): 
    nr, nc = r + dx[d], c + dy[d]
    if nr >= R or nc >= C or nr < 0 or nc < 0 : continue 
    if vis[nr][nc] or alph[board[nr][nc]]: continue 

    done = True 
    vis[nr][nc] = True; alph[board[nr][nc]] = True  
    DFS(nr,nc, tot+1)
    vis[nr][nc] = False; alph[board[nr][nc]] = False 

  if not done : ans = max(ans, tot); return 
  # after 4-direction search, update answer if no where to go 
  # No need to check all values on first recursion 

DFS(0,0,1)
print(ans)