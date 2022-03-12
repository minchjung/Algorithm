# 10971 S2 외판원 순회2 (TSP)
from collections import deque 
N = int(input())
board = [ list(map(int, input().split())) for _ in range(N)]
dp= [ [-1]*(1<<N) for _ in range(N) ] 
INF = 1e11

def DFS(cur, state): 
  if dp[cur][state] != -1 : return dp[cur][state]
  dp[cur][state] = INF
  
  for nxt in range(N) : 
    if state & 1<< nxt : continue 
    dp[cur][state] = min(
      dp[cur][state], DFS(nxt, state or (1<<nxt)) + board[cur][nxt])
  return dp[cur][state]

DFS(0,1)