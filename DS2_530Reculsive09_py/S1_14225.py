# [BruteForce]부분수열의 합[S1]14225 
from itertools import combinations

n= int(input())
S = list(map(int, input().split()))
ref = [False]*(max(S)*n+1)

def backTrack(comb_len): 
    for comb in list(combinations(S,comb_len)) :
        if ref[sum(comb)-1] : continue
        ref[sum(comb)-1] = True   

for i in range(n):  backTrack(i+1)

for idx, num in enumerate(ref):
    if num ==False : 
        print(idx+1)
        break
# BackTrack 오랜만에 ...
# return 조건, 아닌 조건 두개 모두 combination을 거는 생각밖에 안난다.. 
# 그냥 재귀를 빼서 for문을 밖에서 돌렸다 
