# 800 BackTracking[S3]15649_py
N,M= map(int, input().split())
isUsed=[False]*(N+1) 
comb=[0]*(M) 

def gogo(k):
    if k==(M): 
        print(*comb) 
        return 
        # BackTracking 
        # When it meets the return condition above,
        # then it make the one to be original position 
    for i in range(1,N+1):
        if isUsed[i] :continue
        comb[k] = i 
        isUsed[i]=True 
        gogo(k+1) # return here and  
        isUsed[i]=False # <-- to track in backward     
gogo(0)
