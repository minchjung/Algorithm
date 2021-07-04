import sys 
from itertools import combinations   
from collections import deque 

N, M = map(int, sys.stdin.readline().split())
board = [[0]*N for _ in range(N)]
vis = []
virSpot = [] 
dirX = [1, -1, 0, 0]
dirY = [0, 0, 1, -1]
 
for i in range(N) : 
    for j, spot in enumerate(list( map(int, sys.stdin.readline().split())) ): 
        if spot == 2 : # virus 놓을 수 있는 곳을 
            virSpot.append([i, j, 0])  # 미리 담아 두고 
            board[i][j] = "e" # 빈칸으로 바꿔 준다 
        elif spot == 1 :  board[i][j] = "b"  # 벽은 b로 
        else : board[i][j] = "e" # 빈칸은 "e"

ans = N*N*N   # <- 문제 케이스로 나올 수 없는 최대 값으로 설정 
# 바이러스를 놓을 수 있는 자리들의 
# 가능한 조합을 짜서  조합 전체를 하나씩 꺼내고 
for combi in  list(combinations( virSpot , M)) :  

    q = deque() # 조합 전체를 모두 탐색 하는게 BFS 의 시작 과 끝이므로 여기서 Q init 
    # 조합이 바뀔때 마다 vis도 모두 새로 init (주의! 벽일때 True로 매번 바꿔 줘야..) <-- 다른 방법 필요 
    for i in range(N) :
        for j in range(N) : 
            if board[i][j] == "b" : vis[i][j] = True 
            else : vis[i][j] = False
    for com in combi : # 하나의 조합에서 바이러스를 놓기로 결정된 케이스를 모두 꺼내서
        vis[ com[0] ][ com[1] ] = True  # 그 자리를 일단 방문처리하고 
        q.append(com) # 큐의 시작점으로 넣어준다.
        maxAns = 0  # 가장 오래 걸린 시간이 바이러스가 모두 퍼졌을때라 
        # BFS 마다 new 해주고, 매 BFS가 끝날때 이 maxAns의 최소 값이 해가 됨 
    while q : 
        row, col, sec = map( lambda x: x, q.popleft() )  # 큐 : 행,렬,시간 정보 pop 

        for i in range(4) : 
            nxtRow = dirX[i] + row 
            nxtCol = dirY[i] + col # 상 하 좌 우 방향 설정 
            if nxtRow < 0 or nxtRow >= N or nxtCol < 0 or nxtCol >= N : continue # 경계를 넘으면 pass   
            if vis[nxtRow][nxtCol] : continue # 이미 바이러스가 퍼졌으면 pass 
            # 그게 아닌 case 는 "e" 빈칸 이므로, 바이러스를 퍼뜨려 준다
            # 벽은 이미 True로  while 전에 처리가 되었다. 
            vis[nxtRow][nxtCol] = True  # 퍼진 자리라고 표시하고 
            q.append([ nxtRow, nxtCol, sec+1 ]) # 큐에 해당 지점을 새롭게 넣어 준다. 
            maxAns = max(maxAns, sec+1)  # 큐에 push 할때마다 max 값을 update 하고 
        
        boolCheck = True
        for v in vis : 
            if False in v :  # 한 자리라도 빈자리가 있으면  
                boolCheck = False  # 바이러스가 다 못퍼진 케이스라 flag 달고 
                break  
        if(boolCheck) : ans = min (ans, maxAns)  # 모두 퍼졌을때만 퍼진 시간의 최소 값을 update 
# 문제 케이스로 나올 수 없는 최대 값이 
# 그대로 ans가 됬다면 바이러스가 모두 퍼지는 케이스가 없다는것  => -1 출력 
if ans == N*N*N : print(-1) 
else : print(ans)