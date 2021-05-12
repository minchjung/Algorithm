from collections import deque 
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def solution(n,arr): 
    vis=[0]*n 
    board=[[] for _ in range(n)]
    for i in range(n-1): 
        for j in range(i+1,n): 
            if arr[i][j]==0 : continue 
            board[i].append(j)
            board[j].append(i)
    cnt=0
    for i in range(n):
        if vis[i]==1 : continue
        q=deque()
        q.append(i)
        vis[i]=1 
        cnt+=1
        while q : 
            now = q.popleft() 
            for nxt in board[now]: 
                if vis[nxt]==1 : continue 
                vis[nxt]=1
                q.append(nxt)
    return cnt 
# print(solution(  3,  [[1, 0, 0], [0, 1, 0], [0, 0, 1]] ))
# print(solution(  3,  [[1, 1, 0], [1, 1, 0], [0, 0, 1]] ))
# print(solution(  3,  [[1, 1, 0], [1, 1, 1], [0, 1, 1]] ))