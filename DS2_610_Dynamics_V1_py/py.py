# 610[Dynamics][v1]9625
dp1 =(1,0)
dp2 =(0,0)
k = int(input())
for i in range(2,k+2) : 
    a = dp1[1]
    b = dp1[0]+dp1[1]
    dp2 = (a,b)
    dp1 =dp2
print(*dp2)