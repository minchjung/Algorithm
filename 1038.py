from itertools import combinations 

N = int (input()) 
refNum = [str(i) for i in range(10)]
allNum = []

if N >= 1023: print(-1)
else : 
  for i in range(1,11) :
    allNum += [int(("").join(sorted(num, reverse=True))) for num in combinations(refNum, i)] 
  print(sorted(allNum)[N])