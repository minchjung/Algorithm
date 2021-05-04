# 800<BackTracking>[S3]15650 
N,M = map(int, input().split())
ans = [0]*M
isUsed =[False]*(N+1)
#  2 parameters 
# 1) k: counting the M
# 2) startNum: Transferting the starting number of nxt step 
def gogo(k,startNum): 
    if k ==M :
        print(*ans) 
        return 
    for i in range(startNum,N+1): 
        if isUsed[i]: continue 
        isUsed[i]=True 
        ans[k]=i
        gogo(k+1,i+1) # search the next number to fill the rest of combination 
        isUsed[i]=False 
gogo(0,1)