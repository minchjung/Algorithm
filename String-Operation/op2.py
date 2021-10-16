2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
import re
from itertools import permutations

def solution(expression):

    opref =re.findall("[*+-]",expression)
    numref = list(map(int, re.findall(r"\d+", expression)))
    ans = 0 ;
    for priority in permutations(['-','+','*'],3) : 
        op = opref[:]
        num = numref[:]
        for k in range(3):
            temop = []
            temnum= [num[0]]
            for i in range(len(op)):
                if op[i] == priority[k] :
                    nxtNum = num[i]
                    if temnum : 
                        nxtNum = temnum.pop()
                    temnum.append(eval( str(nxtNum)+ op[i] + str(num[i+1])) )
                else : 
                    temop.append(op[i])
                    temnum.append(int(num[i+1]))
            num = temnum[:]
            op = temop[:]
        ans = max(ans, abs(num[0]))
    return ans
