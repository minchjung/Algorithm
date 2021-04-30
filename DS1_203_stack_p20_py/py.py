#203<stack>[V1]20001
n = int(input())
stack= [] 
for i in range(1,n+1):
    line =input().split()
    print("Case #%d: "%i,end="")
    while line : 
        print(line.pop(),end=" ")
    print()