# 2213 트리의 독립집합 failed 
# tree dp 전형적 but ..
# you can pass this 
from sys import setrecursionlimit 
setrecursionlimit(10**9)

N = int(input())
board = [ [] for _ in range(N+1) ]
size = [0] + list(map(int, input().split()))
dp = [[[0,""],[0,""]] for _ in range(N+1)]
vis = [False]*(N+1)

for _ in range(N-1): 
  a, b = map(int, input().split())  
  board[a].append(b)
  board[b].append(a)



def DFS(cur):
  vis[cur] = True 
  dp[cur][1][0] = len(board[cur]) if not size[cur] else size[cur] 
  dp[cur][1][1] = str(cur)
  for nxt in board[cur]:
    if vis[nxt] : continue 
    DFS(nxt)
    dp[cur][1][0] += dp[nxt][0][0]
    dp[cur][1][1] += dp[nxt][0][1] 

    idx = 1 if dp[nxt][0][0] <= dp[nxt][1][0] else 0
    dp[cur][0][0] += dp[nxt][idx][0]
    dp[cur][0][1] += dp[nxt][idx][1]

DFS(1)
print(vis)
print(dp)
# a = 1 if dp[1][0][0] <= dp[1][1][0] else 0
# print(dp[1][a][0])
# ans = list(map(int,list(dp[1][a][1])))
# ans.sort()
# print(*ans)