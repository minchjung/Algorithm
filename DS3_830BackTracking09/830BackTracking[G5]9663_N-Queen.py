# 830<BackTracking>[G5]9663_N-Queen
N = int(input())
# Sequentially check the row, x 
# no need to check whether x is valid or not since the DFS function uses back tracking here 
isUsedY=[0]*N  # valid indicator of the column, y   
isUsedCross1 = [0]*(30) # this indicates the dignole across the map uppper to low 
isUsedCross2 = [0]*(30) # lower to upper 
cnt=0 # if function reaches to last row(x=N), that's the case where the Quenes spotted it all 
#  x=N<-- out of the range, but thats the condition to escape reculsive,here 
def DFS(x):
    global cnt 
    if x==N:
        cnt+=1
        return 
    for y in range(N):
    #    just to check there is anywhere to put the Quene traversing culumn(y) on that row(x) 
        if isUsedY[y]==1 or isUsedCross1[x+y]==1 or isUsedCross2[x-y+N-1]==1: continue
        isUsedY[y]=1 # make that each valid indicator from the spot x,y is not valid anymore   
        isUsedCross1[x+y]=1  
        isUsedCross2[x-y+N-1]=1
        DFS(x+1) # go to the next row
        # reculsive gets back to here if it meets all condition, 
        # but we need to see if it has more valid answer over the rest of the For-Loop (more culmn on that row)
        # So it is necessary to make each valid indicator is back to valid again
        isUsedY[y]=0   
        isUsedCross1[x+y]=0
        isUsedCross2[x-y+N-1]=0
    # dont put the return value here ! 
    # its back tracking !! 
DFS(0)
print (cnt)