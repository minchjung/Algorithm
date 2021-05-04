# 810<BackTracking>[S3]15657-Redundant-Permutation 
N,M= map(int, input().split())
num=list(map(int, input().split()))
num.sort()
ans=[0]*(M) 
def gogo(k,startIdx):
    if k==(M): 
        print(*ans) 
        return 
    for i in range(startIdx,N):
        ans[k] = num[i] 
        gogo(k+1,i) 
gogo(0,0)
