#  시간 초과 .. 
import heapq 
V,E =map(int, input().split())
start =int(input())
board=[[] for _ in range(V+1)] 
isUsed=[11*E]*(V+1)
for _ in range(E):
    a,b,c=map(int, input().split())
    board[a].append([c,b])
hq=[[0,start]] 
isUsed[start]=0
heapq.heapify(hq)
while hq: 
    now = heapq.heappop(hq) #now=[가중치, 노드번호] 가중치가 작은순으로 pop 된다
    if isUsed[now[1]] < now[0]: continue # 입구컷 
    for nodePair in board[now[1]]: # now 노드에 연결된 [가중치,다른노드] 정보를 탐색
        if isUsed[nodePair[1]] <= isUsed[now[1]] + nodePair[0]: continue 
        # 만약 now노드 거쳐 탐색 노드로 갔을때, 기존의 거리보다 더 크면 입구컷
        isUsed[nodePair[1]] = isUsed[now[1]] + nodePair[0]
        # 더 작을때만 그 가중치 거리를 메모에 저장하고 탐색한 노드 정보[가중치, 노드번호]를 hq에 담아준다   
        heapq.heappush(hq, nodePair)
        # 힙push 돌때마다 가중치가 작은 노드 순으로 정렬되 while을 반복한다 
for i in range(1,V+1):
    if isUsed[i]==11*E: print("INF")
    else: print(isUsed[i])
# 48% 시간초과된다.