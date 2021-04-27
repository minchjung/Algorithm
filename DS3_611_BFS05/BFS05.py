n = int(input())
board = [0]+list(map(int, input().split())) 
vis = [0]*(n+1) 
stack = [] 
ans = [] 
for i in range(1,n+1): 
    if vis[i]==1:continue
    stack.append(i)
    vis[i]=1 
    ans.append(i)
    while stack : 
        now = stack.pop()   
        nxt = board[now]
        if vis[nxt]==1 : continue 
        stack.append(nxt)
        vis[nxt]=1
        ans.append(nxt)
