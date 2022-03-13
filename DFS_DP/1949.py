# 1949 우수마을 
# tree DP 전형적 
from sys import setrecursionlimit 
setrecursionlimit(10**9) 

N = int(input())
size = list(map(int, input().split()))
board = [ [] for _ in range(N) ]
vis = [False]*N 
dp = [ [0,0] for _ in range(N)]
for _ in range(N-1): 
  a,b = map(int,input().split())
  board[a-1].append(b-1)
  board[b-1].append(a-1)

def DFS(node):
  vis[node] = True 
  dp[node][0] = 0 
  dp[node][1] = size[node]

  for nxt in board[node] : 
    if vis[nxt] : continue 
    DFS(nxt)
    dp[node][0] += max(dp[nxt][0], dp[nxt][1])
    dp[node][1] += dp[nxt][0]

DFS(0)
print(max(dp[0][0], dp[0][1]))

# 7
# 100 1 1 100 1 1 100
# 1 2
# 2 3
# 3 4
# 3 5
# 5 6
# 6 7