# BOJ:200_Data Strucuture1<Stack Algorithm>-#10828-스택수열-p04 
n = int(input())
stack = []
ans=[]
check =0;
maxVal=0

def pop(s,e):
    for i in range(s,e):
        stack.pop()
        ans.append("-")
def push(s,e):
    for i in range(s,e):
        stack.append(i)
        ans.append("+")
    stack.pop()
    ans.append("-")

for i in range(n):
    num =int(input())
    if stack: # stack null 아니면
        now =maxVal # max값 
        if now == num : # 현재 입력값 과 같으면 
            pop(0,1) # 한번만 pop
            maxVal=num #(중복이 없어서 이경우가 없긴 하다)
        elif now < num :  # 입력이 크면 
            push(now+1,num+1) # push
            maxVal=num
        else: #  입력값이 작으면 
            # num 까지 계속 pop()
            while True:
                if not stack : # stack underflow시
                    check = -1 # 수열 표현이 안됨
                    break; 
                else : # underflow 아니면
                    popNum =stack.pop() # 계속 pop()
                    ans.append("-") 
                    if popNum==num:
                        break; # num 까지 pop
    else: #stack이 null
        if i ==0 :  # 최초 입력 받을때
            push(1,num+1)
            maxVal=num
        else: # 두번째 입력부터 but stack null 
            if maxVal > num : # and stack에서 pop 필요
                check = -1 # 수열 불가
                break
            else: # 아니면 stack에 추가 
                push(maxVal+1,num+1)
                maxVal=num
if check == -1:
    print("NO")
else: 
    for a in ans :
        print(a)