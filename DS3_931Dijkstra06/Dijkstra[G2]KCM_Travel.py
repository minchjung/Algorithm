# 931<Dijkstra>[G4]10282
import heapq 
import sys
T = int(sys.stdin.readline())
for _ in range(T):  
    N,M,K = map(int, sys.stdin.readline().split())
    board = [[] for _ in range(K+1)] 
    for _ in range(K): 
        depart,arrive,c,t = map(int, sys.stdin.readline().split())
        board[depart].append([t,c,arrive])
    hp=[]
    heapq.heappush(hp,[0,0,1])
    ans= 100*1000
    while hp : 
        nowTime, nowCost, nowNode = heapq.heappop(hp)
        if nowNode == N and M >= nowCost : 
            ans = min(ans,nowTime)
            continue 
        for nxtTime, nxtCost, nxtNode in board[nowNode]:
            if M < nowCost + nxtCost : continue 
            if ans <= nowTime + nxtTime : continue 
            heapq.heappush(hp, [nowTime + nxtTime, nowCost+nxtCost ,nxtNode]) 
    if ans== 100*1000: sys.stdout.write("Poor KCM"+'\n')
    else: sys.stdout.write(str(ans)+'\n')                 