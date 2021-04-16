# Sorting07 좌표 정렬2 11651 py 
# 우선순위 
# 1. y , 2. x 
n  = int(input())
number = [] 
for _ in range(n): 
    x,y = map(int,input().split()) 
    number.append((x,y))
number.sort(key=lambda x : (x[1],x[0]))
for num in number :
    print(*num)