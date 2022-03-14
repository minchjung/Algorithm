# 1987 알파벳 G4 
import sys 
R,C = map(int, sys.stdin.readline().split())
board = [ list(sys.stdin.readline().strip()) for _ in range(R) ]

dx = [0,0,1,-1]; dy = [1,-1,0,0]
ans = 0;
Q = set([(1,0,0,board[0][0])])

while Q : 
  tot, r, c, alph = Q.pop()
  for d in range(4): 
    nr, nc = r + dx[d], c + dy[d]
    if nr >= R or nc >= C or nr < 0 or nc < 0 : continue 
    if board[nr][nc] in alph: continue 
    Q.add((tot + 1, nr,nc, alph + board[nr][nc]))
    ans = max(ans, tot + 1)

print(ans)

# vis을 두면 Back-Tracking 형태로 탐색이 불가능함 
# 알파벳만 검사하면 되는것이 전체 로직이라! 
# 실제 Q에 담을때 vis 처리하면 경우의수가 줄어듦. 모든 케이스 검색이 되지 x 
# BFS를 Q로 구현할때, 알파벳만 탐색조건을 걸어주면 된다 
# 아니면 DFS 백트래킹으로 vis, 알파벳을 모두 조건으로 걸면서 탐색해도 되지만
# 재귀 특성상, 시간 초과가 발생하기 쉽다 