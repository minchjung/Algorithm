from collections import deque 
# first step         
sub=[]
ans=[]
ans.append(0)
ans.append(0)
res=10000000
# thrid step 
def add (num,n): 
    global ans 
    global sub
    for am in num : 

# second step  
def primary(n) :
    prNum=deque()
    check = True   
    for number in range(3,n):
        setting = 0 
        for num in range(2,int(number**(0.5))+1):
            if number % num==0 : 
                check= False
                break
            else: check = True
        if check : 
            prNum.append(number)
    add(prNum,n)
for _ in range(1): 
    n = int(input()) 
    primary(n)
print(ans)

