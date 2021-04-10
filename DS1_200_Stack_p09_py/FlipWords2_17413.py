# Data Structure1_201_<Stack>-#17413[문자열뒤집기2]_p09
from collections import deque 
string =input()
dqStr = deque(string) 
dqAns= deque()
stack = [] 

def printAns(check):
    global dqStr
    global dqAns 
    global stack
    if check == -1:
        while dqAns:
            print(dqAns.popleft(), end="")
    else:
        while stack: 
            print(stack.pop(), end="")
        if dqStr:
            tag = dqStr.popleft()
            if tag !="<": 
                print(end=" ")
            dqStr.appendleft(tag)

def stackFunc(now):
    global dqStr
    global stack
    stack.append(now)    
    while dqStr:
        now = dqStr.popleft()
        if now != " " and now !="<":
            stack.append(now)
        else:
            if now =="<":
                dqStr.appendleft(now)
                printAns(1)
                break      
            else:
                printAns(1)
    if stack: 
        printAns(1)

def deqFunc(now):
    global dqStr 
    global dqAns 
    dqAns.append(now)
    while now!=">":
        now = dqStr.popleft()
        dqAns.append(now)
    printAns(-1)

while dqStr:
    now = dqStr.popleft()
    if now =="<":
        deqFunc(now)
    else:
        stackFunc(now)
