# 203<priority_Que>[L2]_Scoville_Programmers 
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt=0
    while len(scoville)>=2 : 
        if scoville[0]>=K : break 
        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville)
        heapq.heappush(scoville, one+(two*2))
        cnt+=1 
    if scoville[0]<K: return -1
    else: return cnt 
