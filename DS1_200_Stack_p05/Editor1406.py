# BOJ:200_Data Strucuture1<Stack Algorithm>-#1406-Editor-p05 

# The cursor starts from the end
stack =[]
stack2=[] 
for s in input(): 
    stack.append(s)
n =int(input())
# Program for the Editor by the input order
for _ in range(n):
    s =input().split() 
    if len(s)==2: # P $ 
        stack.append(s[1])
    elif s[0] == "L": 
        if stack: # for stack underflow
            stack2.append(stack.pop())
    elif s[0] == "D":
        if stack2: # for stack2 underflow
            stack.append(stack2.pop())
    else: # "B"
        if stack:
            stack.pop()
# To set the answer(set for the stack underflow)
# The top item of stack2 goes into the bottom of the stack 
if stack2: 
    for _ in range(len(stack2)): 
        stack.append(stack2.pop())
# To print the answer
if stack : 
    for s in stack :
        print(s, end="") 