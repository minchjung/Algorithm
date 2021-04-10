# Data Structure1_201<Queue>_[문자열뒤집기2]17413_p09_py
from collections import deque 
string =input()
dqStr = deque(string) # original input dq
dqAns= deque() # dq for print <tag> out
stack = [] # stack for print string in backward 

# print function , check whether its Stack or Queue
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
# stack function contains the String to poll backward 
def stackFunc(now):
    global dqStr
    global stack
    stack.append(now)    
    while dqStr:
        now = dqStr.popleft()
        if now != " " and now !="<":
            stack.append(now)
        else: # string meets tag or " "space, then it ends to print
            if now =="<": #"tag  must be into dqStr, again"
                dqStr.appendleft(now)
                printAns(1)
                break      
            else:
                printAns(1)
    # if not <tag> and the String in the end, should be printed
    if stack: 
        printAns(1)
# queue function contains the <tag> to print forward
def deqFunc(now):
    global dqStr 
    global dqAns 
    dqAns.append(now)
    while now!=">":
        now = dqStr.popleft()
        dqAns.append(now)
    printAns(-1)
# execute to function with original input (dq-String)
while dqStr:
    now = dqStr.popleft()
    if now =="<":
        deqFunc(now)
    else:
        stackFunc(now)
