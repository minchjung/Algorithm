
arr = ['O']*1000000  
store = [] 
def down(idx, num):
    cnt = 0  
    if "X" in arr[idx+1 : idx+num+1] : cnt += arr[idx+1: idx+num+1].count("X")
    while arr[idx+cnt+num] =="X": idx +=1
    return idx + cnt + num

def up(idx, num):
    cnt = 0  
    if "X" in arr[idx-num : idx] : cnt += arr[idx-num : idx].count("X")
    while arr[idx-cnt-num]=="X" : idx -=1
    return idx - cnt -num

def delete(idx, n):
    arr[idx] = 'X' 
    store.append(idx)

    if idx + 1 >= n : 
        while arr[idx]=='X': idx -=1  
    
    else : idx += 1  
    return idx 

def solution(n,k,cmd):
    cur = k
    for cm in cmd :   
        if "D" in cm :  cur = down(cur, int(cm[2]))
        elif "U" in cm : cur = up(cur, int(cm[2]))  
        elif "C" in cm : cur = delete(cur, n)  
        else : 
            if store : arr[store.pop()] = "O"

    ans = ""
    for i in range(n): 
        ans+= arr[i]  
    return ans 
# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
