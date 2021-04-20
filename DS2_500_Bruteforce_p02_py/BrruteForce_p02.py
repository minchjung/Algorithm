# 500<Bruteforce>p02_[BlackJack]2798_py
n, m  = map(int, input().split())
numArr = list(map(int, input().split())) 
ans = 0 ; 
def calculation(arr, hap):
    global ans 
    global m 
    for a in arr : 
        if hap + a <= m : 
            ans = max(ans, hap+a)
            if ans == m : 
                return
for i in range(n-2): 
    for j in range(i+1,n-1):
        if ans == m : break 
        hap = numArr[i]+numArr[j]
        calculation(numArr[j+1:],hap)
print(ans)        
