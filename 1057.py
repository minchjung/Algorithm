# 1057 토너먼트 
# https://www.acmicpc.net/problem/1057

L, A, B = map(int, input().split())
A, B = [B, A] if B < A else [A, B]
cnt = 1
while (B % 2 != 0 or B - A != 1) : 
  cnt+=1
  B = (B+1) //2 
  A = (A+1) //2
print(cnt) 