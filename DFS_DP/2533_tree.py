# 2533 tree dp , 사회망 서비스 ! 

#  python 시간초과
#  py3 재귀 불가 recursion runtime error
# 양쪽 간선이어야 한다 => vis로 재방문 체크 
# 자식을 끝까지 보낸다! (for문에 dfs 부터 먼저)
# DFS 함수내 전역 변수로 dp현재값들을 초기화 하고 return 값이 아닌 
# 자식에서 부터 기록하고 있는 dp2값을 참조해주면된다 
from sys import setrecursionlimit 
setrecursionlimit(10**9)
N = int(input())
board = [ [] for _ in range(N+1) ]
dp = [[-1,-1] for _ in range(N+1)]
vis = [False]*(N+1)

for _ in range(N-1):
  a, b = map(int, input().split())
  board[a].append(b)
  board[b].append(a)

def DFS(parent): 
  vis[parent] = True 
  dp[parent][0] = 0; dp[parent][1] = 1 
  for child in board[parent] :
    if vis[child] : continue  
    DFS(child) # DFS 먼저 =leaf까지 보낸다 
    dp[parent][0] += dp[child][1]
    dp[parent][1] += min(dp[child][0], dp[child][1])

vis[1] = True 
DFS(1)
print(min(dp[1][0], dp[1][1]))