n, m = map(int, input().split()) # NxM 
graph = list()
# 행렬맵 graph =입력값 세팅
for _ in range(n):
    graph.append(list(map(int,input())))
dirY = [1,-1,0,0]
dirX = [0,0,1,-1]
visit=[]
result = n*m # 최소값을 최대로 초기화 (전역변수)
cnt=0
def dfs(y,x): #재귀로 DFS수행 
    global result
    global cnt
    for i in range(4): # 상하좌우 4번 수행
        dy = y+dirY[i]
        dx = x+dirX[i] # 좌표 update 후
        if 0<= dy < n and  0<= dx < m and graph[dy][dx]==1: #범위내이면서, map이 1로 갈 수 있으면
            if [n-1,m-1] in visit:  # 마지막에 도달 됬으면
                result =min(result,cnt)    # count값 비교후 작은값으로 update
            else : # 아직 도달 안했으면 
                if([dy,dx] not in visit): # 해당 좌표가 방문한곳이 아니면
                    cnt+=1 # 카운트 해주고 
                    visit.append([dy,dx]) # 방문 추가
                    dfs(dy,dx) # 해당 노드에서 다시 DFS 수행 
                    cnt-=1 # 최초 dfs 수행 노드에서 상하좌우 갈곳 있을 수 있으니 
                    visit.pop() # 카운트와 visit 정보를 다시 초기화 

visit.append([0,0])
cnt+=1
dfs(0,0)
print(result)