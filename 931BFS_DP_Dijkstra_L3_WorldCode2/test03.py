class Node :
    node=0
    nodeCnt=0
    value= 0 
    connTo=[]
    def __init__(self, n):
        self.node = n
    def setNodeCnt(self, c):
        self.nodeCnt = c 
    def setValue(self, v):
        self.value = v 
    def setConnTo(self ,c):
        self.connTo = [c]

# a = [-5,0,2,1,2]
# edges=[[0,1],[3,4],[2,3],[0,3]]
a = [0,1,0 ]
edges=[[0,1],[1,2]]
arr= [0]*len(a) 
cnt=0
def arrNode(now,nxt):
    if arr[now]==0:
        arr[now] = Node(now)
        arr[now].setNodeCnt(1)
        arr[now].setValue(a[now])
        arr[now].setConnTo(nxt) 
    else: 
        arr[now].nodeCnt+=1
        arr[now].connTo.append(nxt)
# process의 key는 nodeCnt를 1일때만 처리해주고 연결된 노드를 -1로 바꿔준다. 
# 노드가 사이클이 아니면 1인 연결노드가 반드시 존재 하기 때문에 
#  Bottom-Up으로 탐색하는데 up에서 연결가지가 2개 이상으로 
# 넓혀지면 다시 nodeCnt가 1인 bottom을 찾아 시작하는 방식
def process(node): # 노드 탐색 process
    global cnt
    connNode=0 
    if node.nodeCnt <=0 : # 방문 불가 상태이고
        if node.value==0:   
            return   # 값이 처리값이 0 이면 그때 해
        else:   return -1 # 처리해야할 값이 있으면 불능
    
    elif node.nodeCnt ==1 :# 갈수 있는 노드가 1개 일때만
        connNode = node.connTo[0] # 그 연결 노드를 찾고

        arr[connNode].nodeCnt -= 1 # 연결 노드의 방문 가능횟수 -1 (현재 노드가 방문 불가 될것이니)
        arr[connNode].connTo.remove(node.node) # 연결 가능 노드 목록도 현재 노드를 지운다
        node.nodeCnt=0 # 현재 노드는 방문 불가 상태로 update

        arr[connNode].value += node.value # 그값 만큼 연결노드는 +
        cnt+= abs(node.value) # 전체 연산 횟수 증가 후
        node.value = 0 # 현재 노드값 0 처리

        process(arr[connNode]) # 연결 노드 호출 
    else: # 방문 가능한데 연결된 노드의 횟수가 2이상이면 
        return # 그냥 for loop으로  return (1부터 처리할것)
for edge in edges : 
    arrNode(edge[0],edge[1])
    arrNode(edge[1],edge[0])

for i, node in enumerate(arr): 
    if node.nodeCnt!=0: 
        t=process(node)
        if t== -1: 
            cnt = -1 
            break
print(cnt)

