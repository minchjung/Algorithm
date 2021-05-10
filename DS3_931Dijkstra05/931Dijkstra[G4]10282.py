# 931<Dijkstra>[G4]10282
import heapq 
T = int(input())
def gogo(n,d,s) : 
    start = s 
    board=[[] for _ in range(n+1)]
    vis=[1000*n]*(n+1)
    # board[의존] = [ [시간,연결컴퓨터], [시간,연결컴퓨터2]...] 
    for _ in range(d): 
        a,b,time = map(int, input().split())
        board[b].append([time,a])
    # Priority Queue[cost, 시작정점] 초기화 
    hp=[[0,start]]
    heapq.heapify(hp)
    vis[start]=0 # 시작노드 방문처리! 안해서 자꾸 틀린다.  
    cnt=1 # 감염 컴퓨터 횟수 저장 
    while hp : 
        cost, now = heapq.heappop(hp) # 시간cost 작은순으로 pop
        for nxt in board[now]: # 현재 노드에 연결된 노드 탐색 
            if vis[nxt[1]]<=cost+nxt[0]: continue  # 이미 탐색됨 +  더 빠른시간 = 입구컷 
            if vis[nxt[1]] == 1000*n : cnt+=1 # 한번도 안가본 상태 = 감염수++
            vis[nxt[1]] = cost + nxt[0] # 최소경로 vis에 update 
            heapq.heappush(hp, [ vis[nxt[1]],nxt[1] ]) # [누적 cost,해당노드] push 
    time=0 # 마지막 노드로 찾아서 인덱스 조회로 시간 줄여보려 했는데 Wrong 
    for v in vis : # 다 돌려서 가본 노드중 max 시간 찾아서 return 
        if v!=1000*n: time=max(time,v)
    return cnt, time 
for _ in range(T) : 
    a,b,c =map(int, input().split())
    num, dur =gogo(a,b,c)
    print(num, dur, sep=" ")