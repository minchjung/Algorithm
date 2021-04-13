# Data Structure1_300<Math>p25_[Factorial_find_0]10827_py
mul=1;
for i in range(1,int(input())+1):
    mul=mul*i

string = list(map(int,str(mul)))
cnt=0
while string: 
    now = string.pop()
    if now !=0:
        print(cnt)
        break
    cnt+=1
