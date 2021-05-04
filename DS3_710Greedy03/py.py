# 710<Greedy>[S5]16435_cpp 
from collections import deque 
N, L = map(int, input().split())
H = sorted(list(map(int, input().split())))
q = deque(H)
while q: 
    now = q.popleft() 
    if L < now : continue  
    L+=1     
print(L)