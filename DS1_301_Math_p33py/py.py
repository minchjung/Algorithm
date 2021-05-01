#  300<Math>[v1]1312
a, b, n = map(int,input().split())
while n>0 : 
    n-=1 
    a %=b 
    a*=10 
print(int(a/b))