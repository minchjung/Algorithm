# <Queue>[Heap_Queue]Priority_Queue[최대힙]11279
import sys 
import heapq as hq
n = int(input())
q =[]
for i in range(n):
    num = int(sys.stdin.readline())
    if num : 
        hq.heappush(q,(-num,num))
    else:
        if q :
            print(hq.heappop(q)[1])
        else:
            print(0)