# DS611[BFS]DSLR_9019 
from collections import deque 
import sys 
def operationD(num): 
    if num*2 >= 10000 : 
        num = (num*2)%10000 
    else: num *= 2
    return num 

def operationS(num): 
    if num==0 : num=9999 
    else : num -=1
    return num

def operationL(num): 
    num = (num % 1000)*10 +num//1000 
    return num

def operationR(num): 
    if num // 1000 !=0 : 
        num = (num%10)*1000 + num//10
    else: num = (num%10)*1000 + num//10
    return num

def checkOP(opTrack,num): 
    if opTrack =="D": num = operationD(num)
    elif opTrack =="S" : num = operationS(num)
    elif opTrack =="L" : num = operationL(num)
    else : num = operationR(num)
    return num 

T = int(input())
opList=["D","S","L","R"]
for _ in range(T):
    A,B = map(int, sys.stdin.readline().split())
    minAns=10000000
    ans=""
    vis=[False]*10020
    q = deque()
    q.append([A,0,""])
    vis[A]=True  
    while q :
        num,cnt,op = q.popleft()
        if cnt >= minAns : break
        if num ==  B :
            minAns = min(minAns,cnt)
            ans=op  
            break  
        for nextOP in opList: 
            tem = checkOP(nextOP,num)
            if vis[tem] : continue 
            vis[tem] =True  
            q.append([tem, cnt+1, op+nextOP])
    print(ans)