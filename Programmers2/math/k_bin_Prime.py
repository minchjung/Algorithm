import math 
def isPrime(N):
    if N == 1: return False  
    for i in range(2,int(math.sqrt(N))+1):
        if not N%i : return False
    return True 

def solution(n, k):
    r = ''; cnt = 0 
    while n > 0 : n, m = divmod(n,k); r += str(m)
    for inf in r[::-1].split('0') : 
        if inf == '1' or inf == '': continue 
        cnt += 1 if isPrime(int(inf)) else 0 
    return cnt 
# n = 437674
# k = 3
# n = 110011
# k = 10
# a = solution(n,k)
# print(a)