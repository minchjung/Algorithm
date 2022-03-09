# 1105 팥
a, b = input().split()
a = list(a); b = list(b)
a.reverse(); b.reverse()
ans = 0 
if len(a) == len(b) :
  while a or b : 
    numA, numB = a.pop(), b.pop()
    if numA == numB : 
      if numA == '8' : ans+=1 
      continue 
    else : break
print(ans)      
