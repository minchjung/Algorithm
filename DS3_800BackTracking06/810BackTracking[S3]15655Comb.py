# 810<BackTracking>[S3]15655-Combination 
N,M= map(int, input().split())
num=list(map(int, input().split()))
num.sort()
ans=[0]*(M) 
isUsed=[False]*(N)
def gogo(k,startIdx):
    if k==(M): 
        print(*ans) 
        return 
    for i in range(startIdx, N):
        if isUsed[i]: continue 
        isUsed[i]=True 
        ans[k] = num[i] 
        gogo(k+1,i+1) # <--here, your starting index is equals to 
        # the current index +1, not the one from origin starting like startIdx+1  
        isUsed[i]=False 
gogo(0,0)
