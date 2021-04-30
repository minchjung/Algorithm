#203<stack>[V1]5089
j = 0 ; 
while True:
    n = int(input())
    if(n==0): break 
    j+=1
    stack=[] 
    for i in range(n): 
        stack.append(input())
    stack =set(stack)
    print("Week %d "%j, end="")
    print(len(stack))