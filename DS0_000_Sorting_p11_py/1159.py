# <sort>[v2]1159_py
alph= [0]*27 
n = int(input())
ans=[]
for i in range(n): 
    c =input()[0]
    alph[ord(c)-ord('a')] +=1 
    if alph[ord(c)-ord('a')] >= 5 : 
        ans.append(c) 
ans=list(set(ans))
ans = sorted(ans)
if ans: 
    for a in ans:
        print(a,end="")
else: print("PREDAJA")