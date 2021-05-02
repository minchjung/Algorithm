# 500[BruteForce][v1]1453
n=input()
spot = list(map(int, input().split())) 
vis = [0]*101 
cnt=0
for s in spot : 
    if vis[s]==1: 
        cnt+=1
        continue 
    vis[s]=1
print(cnt)