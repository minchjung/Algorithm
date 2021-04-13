# Data Structure1_300<Math>p27_[Sum 0f Gcd]9613_py
from collections import deque 
ans=[]
t = int(input())
#gcd function
def gcd(n1,n2): 
    if n1 < n2 : 
        n1,n2 =n2,n1
    while n2!=0: 
        r = n1 % n2
        n1 = n2 
        n2 = r  
    ans.append(n1)
# get input 
for _ in range(t) :
    test = deque(list(map(int, input().split()))) 
    # clear ans list for every test case
    ans.clear()
    if test[0]==1: # if its only one value
        print(0)
        break 
    case = test.popleft() # pop the number of test case
    for i in range(0,case-1): # go search gcd 
        for j in range(i+1,case):
            gcd(test[i],test[j])
    print(sum(ans))