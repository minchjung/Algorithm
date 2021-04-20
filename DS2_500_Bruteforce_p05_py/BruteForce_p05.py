# 500<BruteForce>p05_[덩치]253369_py
n  = int(input())
arr =[]
for _ in range(n): 
    weight,height = map(int, input().split())
    arr.append( (weight,height) )
def compare(wh):
    rank = 1
    for i in range( len(arr) ) : 
        if wh[0] < arr[i][0] and wh[1] < arr[i][1] :
            rank+=1
    return rank
for i in range( len(arr) ) : 
    print( compare(arr[i]), end=" ")
