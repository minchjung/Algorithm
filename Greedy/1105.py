# 1105 팥
# https://www.acmicpc.net/problem/1105
# case를 하나 놓쳐 틀린 답 남김
# 1887 1888 <- 앞에서 부터 같으면서 8이면 ans+1했었지만 
# 같으면서 8이 아니면 ans 카운트 하지 않는걸로 한번 더 나누면 됨 
# if 에 if를 쓰는것을 꺼리지 말자 
a, b = input().split()
a = list(a); b = list(b)
a.reverse(); b.reverse()
ans = 0 
if len(a) == len(b) :
  while a or b : 
    numA, numB = a.pop(), b.pop()
    if numA == numB : 
      if numA == '8' : ans+=1 
      continue 
    else : break
print(ans)      
