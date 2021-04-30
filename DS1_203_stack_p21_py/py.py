#203<stack>[V1]20001
stack= [] 
while True: 
    order = input() 
    if "끝" in order:break
    if "문제" in order: stack.append(0)
    elif order =="고무오리":
        if not stack : 
            stack.append(0)
            stack.append(0)
        else : stack.pop()
if not stack: print("고무오리야 사랑해")
else : print("힝구")