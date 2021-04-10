# BOJ:200_Data Strucuture1<Stack Algorithm>-#10828-Stack-스택p01 
stack = [] 
statement=[]
n = int(input())
for _ in range(n):
    statement.append(input().split())

for strList in statement : 
    if len(strList)==2:
        stack.append(int(strList[1]))
    else:
        if not stack:
            if strList[0]=="size":
                print(0)
            elif strList[0]=="empty":
                print(1)
            else:
                print(-1)
        else:
            if strList[0]=="size":
                print(len(stack))
            elif strList[0]=="empty":
                print(0)
            elif strList[0]=="pop":
                print(stack.pop())
            else:
                print(stack[-1])