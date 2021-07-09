from collections import deque  
dx1=[0,0,1,-1] 
dy1=[1,-1,0,0]

dx2=[1,-1,1,-1]
dy2=[1,-1,-1,1]

dx3=[0,0,2,-2]
dy3=[2,-2,0,0]
board =[[0]]*5
def border(x,y): 
    return x < 0 or x > 4 or y < 0 or y > 4 


def goCheck():
    for i in range(5) : 
        for j in range(5) :
            if board[i][j] != "P" : continue  
            for dir in range(4): 
                row = i + dx1[dir]
                col = j + dy1[dir]
                if border(row,col) is False and board[row][col]== 'P': return 0 

            for dir in range(4): 
                row = i + dx2[dir]
                col = j + dy2[dir]
                if border(row,col) is False and board[row][col]== 'P': 
                    if board[i][col] != 'X' or board[row][j] != 'X' : return 0

            for dir in range(4): 
                row = i + dx3[dir]
                col = j + dy3[dir]
                if border(row,col) is False and board[row][col]== 'P': 
                    if board[i+dx1[dir]][j+dy1[dir]] != 'X': return 0
    return 1 

def solution(places):
    ans=[] 
    for i in range(5): 
        for j, rows in enumerate(places[i]) :
            rows = rows.replace(",","") 
            board[j]= list(str(rows))
        ans.append(goCheck())
    return ans