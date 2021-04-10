# BOJ:200_Data Strucuture1<Stack Algorithm>-#9093 단어뒤집기-p02
from collections import deque
n = int(input())

for _ in range(n):
    # input().split() returns list 
    dq=deque((input().split()))
    # To pick the first word the first
    while dq: 
        words = dq.popleft() 
        # print the word out in backward
        for i in range(1,len(words)+1) : 
            print(words[-i],end="")
        print(end=" ")
    print()