# 611<BFS>[s3]2606_py
from collections import deque 
n = int(input())
k = int(input())
node = [[] for _ in range(n+1)]
for _ in range(k):
    a,b =map(int, input().split())
    node[a].append(b)
    node[b].append(a)

dq = deque() 
dq.append(node[1])
vis=[0]*(n+1)
vis[1]=1 
cnt=0
while dq : 
    now = dq.popleft();
    for m in now : 
        if vis[m]==1 : continue
        vis[m]=1
        dq.append(node[m])
        cnt+=1
print(cnt)




