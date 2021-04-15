# Sorting06 나이순 정렬10814py 
# 우선순위 
# 1. 나이 , 2. 가입 순서 
n  = int(input())
arr = [] 
for idx in range(n): 
    age, name = map(str, input().split()) 
    arr.append((idx,int(age),name))
arr.sort(key=lambda x : (x[1],x[0]))
for a in arr :
    print(a[1], a[2], sep=' ') 
    # age를 int처리 하지 않아 string sort 되서 wrong 
    # Wrong since did not convert string to int from age value 