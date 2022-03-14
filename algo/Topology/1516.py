#  게임개발
import heapq, sys 

N = int(input().strip())
indg = [0]*(N)
board = [ []*N for _ in range(N) ]
time = [0]*N
for build in range(N) :
  for i, a in enumerate(list(map(int, list(sys.stdin.readline().strip().split())))) : 
    temp = []
    if a == -1 : continue 
    if i == 0 : time[build] = a 
    else : 
      indg[build] += 1
      board[a-1].append(build)

pq = []
for i in range(N) : 
  if not indg[i] : heapq.heappush(pq, i)

ans =time[:]
while pq : 
  curN = heapq.heappop(pq);
  for nxtN in board[curN] : 
    indg[nxtN] -= 1 
    ans[nxtN] = max(ans[nxtN], ans[curN] + time[nxtN])
    if not indg[nxtN] : heapq.heappush(pq, nxtN)

for a in ans : print(a)

# 4
# 1 -1
# 1 1 -1
# 1 1 -1
# 1 2 3 -1

# 2
# 10 2 -1
# 10 -1

# ====20 10

# 3
# 5 -1
# 10 -1
# 5 1 2 -1

# ====5 10 15

# 4
# 1 4 3 2 -1
# 2 4 -1
# 1 4 -1
# 1 -1

# ====4 3 2 1

# 5
# 10 -1
# 20 1 -1
# 30 2 -1
# 40 3 5 -1
# 100 -1

# ====10 30 60 140 100

# 4
# 1 4 3 2 -1
# 2 4 -1
# 1 4 -1
# 1 -1