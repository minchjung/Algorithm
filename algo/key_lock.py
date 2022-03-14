# def rotateKey(key) :
#   ref = [k[:] for k in key]
#   s = 0; e = len(ref[0])
#   for r in range(s,e) : 
#     for c in range(s,e) :
#       val = key[r][c]
#       if r >= s and r <= e-2 and c == s : ref[s][e-1-r] = val 
#       elif r == s and c >= s+1 and c <= e -1 : ref[c][e-1] = val 
#       elif r >= s+1 and r <= e-1 and c == e-1 : ref[e-1][e-1-r] = val 
#       elif r == e -1 and c >= s and c <= e-2 : ref[c][s] = val 
#   return ref 

# def checkFit(key,lock):
#   a = [l[:] for l in lock]
#   for r in range(len(lock)):
#     for c in range(len(lock)): 
#       if a[r][c] == 1 and key[r][c] == 1: return False 
#       if a[r][c] == 0 and key[r][c] == 1 : a[r][c] = 1
  
#   for i in a : 
#     if 0 in i : return False 
#   return True 

# def moveToRight(key,lock,move):
#   if move >= len(key) : return False 
#   ref = [ k[:] for k in key]
#   for r in range(len(key)):
#     for c in range(len(key)-move):
#       ref[r][c+move] = key[r][c] 
#   for i in range(len(key)): ref[i][move-1] = 0 
#   if checkFit(ref, lock) : return True 
#   return moveToDown(ref, lock, move)

# def moveToDown(key,lock,move):
#   if move >= len(key) : return False 
#   ref = [ k[:] for k in key]
#   for r in range(move, len(key)):
#     ref[r] = key[r-1][:]
#   for i in range(move): 
#     ref[i] = [0]*len(key)
#   if checkFit(ref, lock) : return True 
#   return moveToDown(ref,lock,move+1)

# def solution(key, lock):
#   rotcnt = 0 
#   lenB = len(lock)+2*(len(key)-1)
#   board = [ [0]*lenB for _ in range(lenB)]
#   while rotcnt < 4 : 
#     s = 0;  e = len(key[0]) 
#     while s < e :
#       t = rotateKey([ key[k][s:e] for k in range(s,e) ]) 
#       for i in range(s,e):
#         key[i][s:e] = t[i-s][:]
#       s += 1; e-=1   
#     if checkFit(key,board) : return True 
#     for i in range(1,len(key)):
#       if moveToRight(key,lock, i) : return True        

#     rotcnt+=1 

#   return True 



# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1, 1, 1,0], [1, 1, 0,1], [1, 0, 1,0],[1,0,0,1]]
# key = [[0,1,0,0],[1,0,0,0],[1,1,0,0],[0,1,0,0]]
# a = solution(key, lock)
# print(a)