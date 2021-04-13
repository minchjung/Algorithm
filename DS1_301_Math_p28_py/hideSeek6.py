# Data Structure1_301<Math>p28_[숨바꼭질 6]17087_py
# n=number to find, start=start position 
n,start = map(int,input().split())
def gcd():
    n1 = ans.pop()
    n2 = ans.pop()
    if n1 < n2 : 
        n1, n2 = n2, n1 
    while n2!=0: 
        r = n1 % n2  
        n1 = n2 
        n2 = r 
    ans.append(n1)    
# Loop input list, and get gcd when every 2 position
# gcd from every new value with the gcd from previous one [Recursive]
ans= []
for sis in list(map(int, input().split())):
    ans.append(abs(start-sis))
    if len(ans)>=2: 
        gcd()
print(ans[0])