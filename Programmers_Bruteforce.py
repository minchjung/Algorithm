def solution(rows, columns, queries):
  ans = []
  board = [[j+i*columns for j in range(1, columns+1) ] for i in range(rows)]

  for q in queries : 
    x1,y1,x2,y2 = q
    minVal = 1e5
    ref = [ b[:] for b in board ]
    for r in range(x1-1, x2) :
      for c in range(y1-1, y2) :
        if x1 -1 <= r < x2 -1 and c == y1 - 1 : 
          board[r][c] = ref[r+1][c]
          minVal = min(minVal, board[r][c])  
        if x1  <= r < x2  and c == y2 - 1 : 
          board[r][c] = ref[r-1][c] 
          minVal = min(minVal, board[r][c])  
        if x1 - 1 == r and y1 <= c < y2 : 
          board[r][c] = ref[r][c-1]
          minVal = min(minVal, board[r][c])  
        if x2 -1 == r and y1 -1 <= c < y2-1 : 
          board[r][c] = ref[r][c+1]
          minVal = min(minVal, board[r][c])  
    ans.append(minVal)
  print(ans)
  return ans
solution(6, 6, [[2,2,5,4], [3,3,6,6], [5,1,6,3]])