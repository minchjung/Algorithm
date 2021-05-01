# <stack,que>[v1]1268
from collections import deque 
n = int(input())
inf= []
for i in range(n): 
    inf.append(list(map(int,input().split())))
ans=[]
for i in range(n): 
    q=deque() 
    q.append(inf[i])
    vis =[0]*n
    while q : 
        now = q[-1]
        cnt=0
        for i in range(5):
            for j in range(n): 
                if now[i]==inf[j][i] and vis[j]==0:
                    vis[j]=1 
                    cnt+=1
        q.pop()
    ans.append(cnt-1) 
print(ans.index(max(ans))+1)       