# 9663 N Queen , G5 
# 대각선 선형 리스트로 체크 
# 가로와 세로 중에 하나만 비교! no 이중 for문 
# DFS 인자를 대각선 체크위해, n-1 형태x, n +1로 증가시키며 탐색 
# 탈출 n == N ! 
N = int(input())
board = [ [0]*N for _ in range(N) ]
isUsedCross1 = [False]*(N*2) 
isUsedCross2 = [False]*(N*2)
isUsedLine = [False]*N
ans = 0 

def DFS(n):
  global ans
  if n == N : ans +=1; return 
  for r in range(N):
    if isUsedLine[r] or isUsedCross1[r+n] or isUsedCross2[n-r+N-1]: continue 
    isUsedLine[r] = True; isUsedCross1[r+n] = True; isUsedCross2[n-r+N-1] = True 
    DFS(n+1)
    isUsedLine[r] = False; isUsedCross1[r+n] = False; isUsedCross2[n-r+N-1] = False 
DFS(0)
print(ans)