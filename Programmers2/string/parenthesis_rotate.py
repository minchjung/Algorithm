# 괄호 회전하기
# my own solution is the best so far ! 
from functools import reduce 
def solution(s) :
    S = s[:]; cnt = 0
    for _ in range(len(s)):
        S = S[1:]+S[0]; 
        _S = S[:]; l = len(_S)
        while _S : 
            _S = reduce(lambda t,x : t.replace(x,""),['()','{}','[]'],_S)
            if l == len(_S): break 
            l = len(_S)
        cnt += 1 if not len(_S) else 0 
    return cnt





# s = "[]()([[{(([{(([[{([])}]]))()}]))()}]])({()}))([])[{}"
s = "[](){}"
# s = "}]()[{"
# s = "[)(]"
# s = "}}}"
a = solution(s)
print(a)

    # R = [reduce(lambda ac, x: ac+')' if x =='(' else(ac+'}' if x =='{' else ac+']'), open[::-1],''.join(open)) for i in range(1,4) for open in permutations(['(','{','['],i)]
    # cnt = 0 
    # for _ in range(len(S)):
    #     S = S[1::]+S[0]
    #     a = reduce(lambda acc, x : acc.replace(x,''),R,S)
    #     cnt += 0 if not '' == reduce(lambda acc, x : acc.replace(x,''),R,S) else 1 
    #     print(a)
    # print(R)
    # return cnt

