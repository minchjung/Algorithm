# DataStructure1_200_<Queue>p07_[요세푸스]1158_py
from collections import deque
n,k =list(map( int, input().split())) 
dq =deque([i for i in range(1,n+1)])
stack=[]
number=0
# pop until item empty or onley one left
while dq :
    # stop if its last one
    if len(dq)==1:  
        stack.append(dq.popleft())
        break
    now = dq.popleft() 
    number+=1
    if number !=k: 
        dq.append(now)
    else: 
        stack.append(now)
        number=0
# print the answer out 
ans ="<"
j=1
for s in stack : 
    if j==len(stack):
        ans+= str(s)+">"
    else:
        ans+= str(s)+", "
    j+=1
print(ans)
