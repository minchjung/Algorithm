# Programmers소수찾기Lv2
from math import pow
from itertools import permutations 
cnt = 0 
isChecked = [False]* 10000001
def prime(n) : 
    global cnt 
    check = True 
    for i in range(2, round(pow(n, 1/2)+1)) : 
        if n % i == 0 :  check = False 

    if(check) : 
        cnt +=1 

def solution(numbers):
    isChecked[0] = True; 
    isChecked[1] = True; 
    for i in range(1, len(numbers)+1) : 
        for nums in map(int, map(''.join, permutations(list(numbers),i))) : 
            if(isChecked[nums]) : continue 
            prime(nums)
            isChecked[nums] = True;        
    return cnt 