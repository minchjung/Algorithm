# 500<BruteForce>p03_[분해합]2231_py
target = int(input())
arr = [0]*101
# 음수 처리 if 조건 귀찮 -> 100까지 미리 구해놓고 
# 100 이상부터 target -자리수 *9 ~ target -1 까지 검사해 없으면 끝
for num in range(10,len(arr)):
    tem = 0 
    for n in str(num):
        tem+=int(n)
    arr[num]=num+tem
check = 0
if target <=100 :
    if target in arr: 
        print(arr.index(target))
    else:
        print(0)
else: 
    for num in range(target-len(str(target))*9  ,target-1):
        tem= 0
        for n in str(num):
            tem +=int(n)
        if num+tem ==target : 
            check+=1
            print (num)
            break
    if check ==0 : 
        print(0)