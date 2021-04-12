import sys
from math import sqrt
input=sys.stdin.readline

d={'*':2,'/':2,'+':1,'-':1,'(':0,')':0}
q=[]
s=input().strip()
for x in s:
    if x not in d:
        print(x,end='')
    elif x=='(':
        q.append(x)
    elif x==')':
        while q:
            cur=q.pop()
            if cur=='(': break
            print(cur,end='')
    else:
        while q and q[-1]!='(' and d[x]<=d[q[-1]]:
            print(q.pop(),end='')
        q.append(x)
while q:
    print(q.pop(),end='')