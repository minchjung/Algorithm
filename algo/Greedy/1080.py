# 1080 행렬
# A를 B와 비교해 동일하게 바꿀때 3x3만 뒤집기.
# 3x3을 넘어서면 못뒤집고, 
# 1. 순차적으로 row부터 비교해서 뒤집는다 
# 2. 3x3을 따로 for문해서 뒤집자 
# 3. 마무리에 검사를 전체 행렬을 그냥 다해서 검서하자 ! (50x50)   

N, M = map(int,input().split())
A= [ list(map(int, list(input()))) for _ in range(N) ]
B= [ list(map(int, list(input()))) for _ in range(N) ]
check =[[False]*M for _ in range(N)]
cnt = 0
for r in range(N) : 
  for c in range(M) : 
    if A[r][c] == B[r][c] : continue
    nA = [a[:] for a in A ]
    if (c + 3 <= M and r + 3 <= N): 
      cnt+=1
      for nr in range(r, r+3) :
        for nc in range(c, c+3) :
          nA[nr][nc] = 0 if nA[nr][nc] else 1 
      A = [ a[:] for a in nA]

ans = 51*51
for i in range(N) : 
  for j in range(M) : 
    if A[i][j] != B[i][j] : ans = -1 
print(min(ans, cnt))

