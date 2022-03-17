# 표 편집 L3
def solution(n,k, cmd):
    ans = { i : [ n-1 if i == 0 else i-1, 0 if i == n-1 else i+1 ]for i in range(n) } 
    stack = []; maxN = n-1 
    for cm in cmd : 
        if cm[0] == 'D' or cm[0] == 'U':
            b = int(cm.split(" ")[1])
            print(b)
            while b > 0 and cm[0] == 'D': k = ans[k][1]; b-=1 
            while b > 0 and cm[0] == 'U': k = ans[k][0]; b-=1
        elif cm[0] == "C" :
            tem = k  
            ans[ans[k][0]][1] = ans[k][1]
            ans[ans[k][1]][0] = ans[k][0]
            if k == maxN : k = ans[k][0]; maxN = k
            else : k= ans[k][1] ;
            stack += [[tem,ans[tem]]]
            del ans[tem]
        else : 
            key, val = stack.pop()
            ans[val[0]][1] = key 
            ans[val[1]][0] = key 
            ans[key] = val 
            maxN = max(maxN,key)
    return  "".join([ 'O' if i in ans else 'X'for i in range(n) ])
# 조건을 잘따져줘야!! 