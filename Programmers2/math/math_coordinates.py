# 교점 별만들기
from itertools import combinations 
def solution(line):
    ans = []; mx=[1e16,-1e16]; my =[1e16,-1e16]
    for comb in combinations(line,2):
        a,b,e = comb[0]; c,d,f = comb[1]
        dn = a*d-b*c; n1 =b*f-e*d; n2 = e*c-a*f   
    
        if not dn or n1%dn or n2%dn: continue  
        ans += [[n1//dn, n2//dn]] 
        mx[0] = min(mx[0],ans[-1][0]); mx[1] = max(mx[1],ans[-1][0])
        my[0] = min(my[0],ans[-1][1]); my[1] = max(my[1],ans[-1][1])
    
    return [ ''.join(['*' if [j,i] in ans else '.' for j in range(mx[0],mx[1]+1)])  for i in range(my[1],my[0]-1,-1) ] 

l = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
l= [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
l =[[1, -1, 0], [2, -1, 0]]
l = [[1, -1, 0], [2, -1, 0], [4, -1, 0]]
a = solution(l)
print(a)