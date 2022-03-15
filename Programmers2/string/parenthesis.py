
def makeUV(R):
    s = 0; e = 0; 
    u=""; v="" 
    for i in range(len(R)):
        if R[i] == '(' : s+=1
        else : e+=1 
        if s == e : 
            u, v = R[:i+1], R[i+1:]
            break 
    return [u,v]

def check1(R):
    stack = [] 
    for s in R : 
        if s =='(': stack.append(s)
        else : 
            if not stack : return False 
            stack.pop() 
    return True 

def solution(P) :
    W = P[:]
    if check1(W) : return W
    u, v = makeUV(W)
    if check1(u) : u += solution(v); return u 
    else :
        v = solution(v) 
        newW = "(" +v +")"
        for i in range(1,len(u)-1): 
            if u[i] == '(' : newW += ')'
            else : newW += '('
        return newW

P = ")("
P="()))((()"	
print(solution(P))