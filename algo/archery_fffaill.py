# 양궁대회 lev2
from itertools import combinations_with_replacement
def solution(n, info):
    maxAns=0; dirAns =[]
    for comb in combinations_with_replacement(range(11), n) : 
        ans = [0]*11; t1=0;t2=0
        for c in comb : ans[c]+=1
        for i in range(11): 
            if info[i]:
                if info[i] >= ans[i] : t1+= (10-i)
                else : t2 += (10-i)
            else : 
                if ans[i]> 0 : t2 += (10-i)
        if t1 < t2 :
            if maxAns > t2 - t1 : continue 
            if maxAns <= t2 - t1 : dirAns = [(' ').join(list(map(str,ans)))] 
            maxAns = max(maxAns, t2-t1)
    return [-1] if not dirAns else list(map(int, dirAns[0].split()))    
 
# n = 5 
# info = [2,1,1,1,0,0,0,0,0,0,0]	
n = 1 
info = [1,0,0,0,0,0,0,0,0,0,0]

n =9	
info = [0,0,1,2,0,1,1,1,1,1,1]
a = solution(n,info)
print(a)