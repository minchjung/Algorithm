# 입국심사 - 이분탐색
from functools import reduce
def solution(n, times):
  s =0; e = times[-1]*n 
  while s < e : 
    m = (s+e)//2 
    p = reduce(lambda t,x : t+(m//x), times,0)
    e,s = [m,s] if p >= n else [e,m+1]  
  return s