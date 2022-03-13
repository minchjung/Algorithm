#  6603 로또 S2
from itertools import combinations

while True :
  board = list(map(int, input().split()))
  k = board[0]
  if k == 0 : break
  for a in combinations(board[1:], 6) :
    print(*a)
  print()