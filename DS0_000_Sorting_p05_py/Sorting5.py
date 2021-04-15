# Sorting04 좌표정렬11650 py 
# 우선순위 
# 1. x , 2. y 
n  = int(input())
number = [] 
for _ in range(n): 
    x,y = map(int,input().split()) 
    number.append((x,y))
number.sort(key=lambda x : (x[0],x[1]))
for num in number :
    print(*num)