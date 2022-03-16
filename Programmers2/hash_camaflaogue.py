# 위장
def solution(clothes):
    d = dict()
    for c in clothes :
        try : d[c[1]].append(c[0]) 
        except : d[c[1]] = [c[0]] 
    ans = 1; num = [] 
    for key, val in d.items():
        num.append(len(val)+1)
    for n in num :ans *= n 

    return  ans -1 
c = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
a = solution(c)
print(a)