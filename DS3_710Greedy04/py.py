# 710<Greedy>[S3]11508
N = int(input())
pr=[]
for _ in range(N): 
    pr.append(int(input()))
pr.sort(reverse=True)
ans=0 
for num,p in enumerate(pr) : 
    num%=3
    ans+=p
    if num ==2 : ans-=p
print(ans)    