import sys 
from itertools import permutations 

N, M, K = map(int, sys.stdin.readline().split())  
board =  [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]
rotate = [ list(map(int, sys.stdin.readline().split())) for _ in range(K) ]
temAns = [ ]

def dfs(r, c, s) :
    if s == 0 : return  
    start = [r-s-1, c-s-1]
    end = [r+s-1, c+s-1]
    ref = [ t[:] for t in temAns ]
    for i in range(start[0], end[0]+1) :
        for j in range(start[1],end[1]+1) : 
            if start[0] <= i < end[0] and start[1] == j : 
                temAns[i][j] = ref[i+1][j]
            elif start[0] == i and start[1] < j <= end[1] : 
                temAns[i][j] = ref[i][j-1]
            elif start[0] < i <= end[0] and end[1] == j : 
                temAns[i][j] = ref[i-1][j]
            elif end[0] == i and start[1] <= j < end[1] : 
                temAns[i][j] = ref[i][j+1]
    dfs(r,c,s-1)      

ans = 100*100 
rot_combi = list(permutations( rotate, K ))
while rot_combi : 
    temAns = [ b[:] for b in board]
    for setCombi in rot_combi.pop() : 
        row, col, sss = map(lambda x : x , setCombi)
        dfs(row, col, sss)
    for rowList in temAns : 
        ans = min(ans, sum(rowList)) 
print(ans)
