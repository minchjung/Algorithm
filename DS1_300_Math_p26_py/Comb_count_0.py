# Data Structure1_300<Math>p26_[Combination_Count_0]2004_py
mul=1;
divd = 1;
n,m =map(int, input().split() )
for i in range(n-m+1,n+1):
    mul=mul*i
for i in range(1,m+1):
    divd=divd*i
cnt=0;
for i in str(mul//divd)[::-1]:
    if i !="0":
        print(cnt)
        break
    cnt+=1