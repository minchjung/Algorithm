# Sorting09 숫자카드 10815 py 이진탐색 
# Time out error : binary search Needs !! ===Worked
n  = int(input())
sang = list(map(int,input().split())) 
t = int(input())
numbers = list(map(int,input().split())) 
# 이진탐색은 정렬된 값들에서 특정 값을 찾을때,
# 횟수를 거듭 할때 마다 search data를 1/2로 줄일 수 있다. 
sang.sort()
# since sang array is sorted, 
for i, num in enumerate(numbers): 
    start = 0 
    end = n -1
    while start <= end : 
        mid = (end+ start )//2 # first to find mid value
        if sang[mid] == num: 
            print(1,end=" ") # end if thats number to find 
            break 
        elif num > sang[mid]: # reset start index to find bigger value
            start = mid +1 
        elif num < sang[mid]: # reset end index to find smaller value
            end = mid-1
    if start > end : # if they're reversed , no value to find  
        print(0,end=" ")