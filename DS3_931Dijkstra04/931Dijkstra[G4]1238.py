# 931Dijkstra[G4]1238
import heapq 
N, M, X = map(int, input().split())
# board=지도, ans= 각 노드의 최단거리값들 기록  
board = [[] for _ in range(N+1)] 
ans=[0]*(N+1)
for i in range(M):
    a,b,c = map(int, input().split())
    board[a].append([c,a,b])
# dijkstra 시작 
for depart in range(1,N+1):
    # 출발 노드를 순차적으로 선택해 BFS를 진행
    # 따라서 BFS수행마다 메모가 필요한 dist 와 heapq 초기화
    dist= [100*M]*(N+1)
    hp=[]
    heapq.heappush(hp, [0,depart]) #[누적시간(Cost), 현재노드] push  
    dist[depart]=0 # 출발노드 거리=0
    while hp : 
        time, now = heapq.heappop(hp) # 낮은 Cost 순으로 pop
        for nxt in board[now]: # 연결된 다음 노드 탐색 
            # 다음 노드가...  
            # 1.출발 노드로 복귀  = 입구컷 
            # 2.이미 탐색 후, 저장한 최적 경로보다 더 큰값 = 입구컷 
            if nxt[2] ==depart or dist[nxt[2]] <= time + nxt[0] : continue 
            dist[nxt[2]]= time + nxt[0] # 출발점~ 해당노드 까지 최적경로 Update 
            heapq.heappush(hp, [dist[nxt[2]],nxt[2]]) # [위누적Cost, 노드번호]push
    # BFS 끝나고 X까지 가는 최적(최소)경로 저장
    ans[depart]+=dist[X]
    if depart == X : # 출발점이 X일때 각 노드로 돌아가는 최적경로 이므로 
        for k in range(1,N+1): # 가는 최적 경로에 ++ 
            ans[k]+=dist[k]  
print(max(ans)) # 누적 최대 = answer
                
