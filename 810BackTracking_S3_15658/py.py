N = int(input())
number = list(map(int, input().split()))
opOri=[]
opAns=[0]*(4*N)
opUsed=[0]*(4*N)

maxAns=-1000000000
minAns= 1000000000
def calculate():
    num=number[0];
    for i in range(len(number)-1):
        tem =opAns[i]
        if tem==1: num+=number[i+1]
        elif tem ==2 : num-=number[i+1]
        elif tem ==3 : num*=number[i+1]
        else: num=num//number[i+1]
    return num

def backTrack(k):
    global maxAns, minAns 
    if k==N-1:
        hap= calculate() 
        maxAns=max(maxAns,hap)
        minAns=min(minAns,hap)
        return 
    for i in range(len(opOri)): 
        if opUsed[i]!=0:continue 
        opUsed[i]=1
        opAns[k]=opOri[i]
        backTrack(k+1)
        opUsed[i]=0
op = list(map(int, input().split()))
for i,o in enumerate(op) : 
    for _ in range(o):
        opOri.append(i+1)
backTrack(0)
print(maxAns)
print(minAns)