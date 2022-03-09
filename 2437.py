#  저울 
# https://www.acmicpc.net/problem/2437

N = int(input())
W = list(map(int,input().split()))
W.sort()
sum = 1;

for w in W : 
  if w > sum : break 
  sum += w
print(sum)