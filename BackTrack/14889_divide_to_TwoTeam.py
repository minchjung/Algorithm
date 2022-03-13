# 스타트와 링크
# S2 14889
# 두팀 나누기, idx도 DFS 인자로 같이 넣어줘야! 
N = int(input())
S = [ list(map(int, input().split())) for _ in range(N) ]
vis = [False]*N
ans = 1e9; tot = 0;  

for i in range(N) :
  for j in range(N) : 
    tot += S[i][j]

def DFS(cnt, p):
  global ans, tot
  if cnt <= 0 : 
    start = 0; link = 0 
    for r in range(N):
      for c in range(N): 
        if vis[r] and vis[c] : start += S[r][c] 
        if not vis[r] and not vis[c]: link += S[r][c]
    ans = min(ans, abs(start-link))
    return 

  for i in range(p, N):
    if vis[i] : continue 
    vis[i] = True 
    DFS(cnt-1, i+1)
    vis[i] = False

DFS(N//2, 0)
print(ans)