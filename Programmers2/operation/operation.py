# 수식최대화
from itertools import permutations
def solution(expression):
    ans = 0 
    for op in permutations(['-','+','*']):
        b = []
        for exp in expression.split(op[0]):
            a = [ f'({ex})' for ex in exp.split(op[1])]
            b += [ f'({op[1].join(a)})' ]
        ans = max(abs(eval(op[0].join(b))), ans) 
    return ans 

e = "100-200*300-500+20-30-20+50+60*70+90-0+1-11*3"
e="50*6-3*2"
a = solution(e)
print(a)