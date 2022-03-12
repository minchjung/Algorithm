#  14888 연산자 끼워넣기 s1 
#  back tracking 
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
ans = [1e11, -1e11]

def DFS(cur, tot):
  if cur >= N :
    ans[0] = min(ans[0], tot)
    ans[1] = max(ans[1], tot)    
    return 
  curN = num[cur]
  for i in range(4) :
    if op[i] != 0 :
      op[i]-=1
      if i == 0 : 
        DFS(cur+1, tot + curN)
      elif i == 1 : 
        DFS(cur+1, tot - curN)
      elif i == 2 :
        DFS(cur+1, tot * curN)
      else :
        f = -1 if tot < 0 else 1 
        DFS(cur+1, ((f*tot)//curN)*f)
      op[i]+=1
 
DFS(1,num[0])
print(ans[1], ans[0])