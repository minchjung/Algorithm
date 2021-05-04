# 810<BackTracking>[S3]15654
N,M= map(int, input().split())
num=list(map(int, input().split()))
num.sort()
ans=[0]*(M) 
isUsed=[False]*(N)
def gogo(k):
    if k==(M): 
        print(*ans) 
        return 
    for i in range(N):
        if isUsed[i]: continue 
        isUsed[i]= True 
        ans[k] = num[i] 
        gogo(k+1) 
        isUsed[i] = False 
gogo(0)
