#<BruteForce>[1759][암호만들기]p0_
n = int(input())
arr = list(map(int, input().split()))
ans = [] 
def func(ar):
    for i in range (len(ar)):
        if i == len(ar)-1: return 
        func(ar)        

for i in range(n): 
    arr[i]
