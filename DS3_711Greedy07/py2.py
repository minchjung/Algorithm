# 711[Greedy][G1]동전 뒤집기_1285_py 
from itertools import combinations 
import sys 

def goCheck(culTo_change):
    global N 
    status=[False]*(N+1)
    tot = 0 
    for row in culTo_change : 
        status[row] =True
 
    for i in range(N):
        cnt=0
        for j in range(N): 
            cur = board[i][j]
            if status[j] : 
                if cur == 'T': cur ='H'
                else : cur = 'T'
            if cur == 'T' : cnt+=1
        tot += min(cnt, N-cnt)
    return(tot)

N = int(sys.stdin.readline().strip())
board=[ list(sys.stdin.readline().strip()) for _ in range(N)]
numList = list(range(N))
ans = N*N

for i in range(N): 
    for combination in list(combinations(numList,i+1)) : 
        ans = min(ans, goCheck(combination))
print(ans)
