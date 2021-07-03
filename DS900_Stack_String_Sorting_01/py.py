import sys 

string  = list(sys.stdin.readline().strip()) 
bomb =  sys.stdin.readline().strip() 
N = len(bomb) 
stack = [] 

for s in string : 
    stack.append(s) 
    if s == bomb[-1] and ''.join(stack[-N::]) == bomb : del stack[-N::] 
    
if stack : print(''.join(stack))
else : print("FRULA")