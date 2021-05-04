# 800<BackTracking>[S3]15651 
N,M = map(int, input().split())
ans = [0]*M
def gogo(k): 
    if k ==M :
        print(*ans) 
        return 
    for i in range(1,N+1): 
        ans[k]=i
        gogo(k+1) 
gogo(0)
# Redundant combination 
# => No need to check whether the Numbers are redundantly used or not 