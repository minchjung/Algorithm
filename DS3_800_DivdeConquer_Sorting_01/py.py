# 800 Divid Conquer 2108-숫자카드
n  = int(input())
sang = list(map(int,input().split())) 
t = int(input())
numbers = list(map(int,input().split())) 
sang.sort()
for i, num in enumerate(numbers): 
    start = 0 
    end = n -1
    while start <= end : 
        mid = (end+ start )//2
        if sang[mid] == num: 
            print(1,end=" ")
            break 
        elif num > sang[mid]: 
            start = mid +1 
        elif num < sang[mid]:
            end = mid-1
    if start > end : 
        print(0,end=" ")