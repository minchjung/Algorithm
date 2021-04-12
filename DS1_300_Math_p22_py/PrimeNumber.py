m,n=map(int, input().split())
ans=[]
for num in range(m,n-1):
    b = True
    if num ==3:
        ans.append(3) 
    elif num > 3 and  num % 2 !=0: 
        for j in range(2,int(num**(0.5))+1):
            if num % j ==0:
                b =False
                break
            else: b =True
        if b : 
            ans.append(num)
for a in ans:
    print(a)
