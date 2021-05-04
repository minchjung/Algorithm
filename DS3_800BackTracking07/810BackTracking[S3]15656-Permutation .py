# 810<BackTracking>[S3]15656-Permutation 
N,M= map(int, input().split())
num=list(map(int, input().split()))
num.sort()
ans=[0]*(M) 
def gogo(k):
    if k==(M): 
        print(*ans) 
        return 
    for i in range(N):
        ans[k] = num[i] 
        gogo(k+1) 
gogo(0)
