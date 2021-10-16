import re
from itertools import permutations

def solution(expression):
  ans = 0
  for op in permutations(['+','-','*'],3) :
    p1 = op[0]
    p2 = op[1]
    temList = []
    for exp in expression.split(p1) :
      tem = [f"({e})"for e in exp.split(p2)]
      temList.append( f"({p2.join(tem)})" )
    ans = max(ans, abs(eval(p1.join(temList))))
  return ans  
# expression = "100-200*300-500+20"
expression = "50*6-3*2"
a = solution(expression)
print(a)


