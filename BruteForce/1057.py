# 1057 토너먼트 
# https://www.acmicpc.net/problem/1057
# 1. 2그룹으로 묶는 그룹화 특징 
# 2. 만나는 특정 조건시 그리디 탐색 끝 

L, A, B = map(int, input().split())
A, B = [B, A] if B < A else [A, B]
cnt = 1
while (B % 2 != 0 or B - A != 1) : 
  cnt+=1
  B = (B+1) //2 
  A = (A+1) //2
print(cnt) 