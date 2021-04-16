# Sorting08 보물 1026 py 
# . A[0]xB[0]+ ..최소값 
n  = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
ans=0
for i,num in enumerate(a):
    ans+= num *b[i]
print(ans)