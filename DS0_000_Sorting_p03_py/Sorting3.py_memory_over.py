# Sorting01 [10989]_py  Not Work by Memory exceeded
# Memory limit = 8MB  <---- This is the challenge part
import sys
n = int(sys.stdin.readline()) 
arr=[0]*10001 # use one array and update 
for _ in range(n):
    # index is the number 
    # count it if its more  
    arr[(int(sys.stdin.readline()))] +=1; 
for i in range(10001):
    # print index (count)times when avaiable 
    if arr[i] !=0 : 
        for _ in range(arr[i]):
            print(i)