def solution(numbers,target): 
    cnt=0
    def backTrack(k, tot):
        nonlocal target
        nonlocal cnt 
        if k == len(numbers): 
            if tot == target : cnt+=1 
            return 
        backTrack(k+1,tot+numbers[k])
        backTrack(k+1,tot-numbers[k])
    backTrack(0,0)
    return cnt
