import sys
from collections import deque
sys.stdin = open("input.txt", "r")

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
Q1 = deque()
Q2 = deque()
zero_count = 0
count = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(m):
  for j in range(n):
    if board[j][i] == 1:
      Q1.append((i, j))
    elif board[j][i] == 0:
      zero_count += 1

if len(Q1) == 0:
  print(-1)
  sys.exit(0)

if zero_count == 0:
  print(0)
  sys.exit(0)

def infect_toamto(from_Q, to_Q):
  global count
  global dx, dy
  while len(from_Q) != 0:
    prev_x, prev_y = from_Q.popleft()
    for i in range(4):
      x = prev_x + dx[i]
      y = prev_y + dy[i]
      if 0 <= x <= m - 1 and 0 <= y <= n - 1 and board[y][x] == 0:
        board[y][x] = 1
        to_Q.append((x, y))

infect_toamto(Q1, Q2)

while len(Q1) != 0 or len(Q2) != 0:
  if len(Q2) == 0:
    infect_toamto(Q1, Q2)
  elif len(Q1) == 0:
    infect_toamto(Q2, Q1)
  count += 1
  
for i in range(m):
  for j in range(n):
    if board[j][i] == 0:
      print(-1)
      sys.exit(0)

print(count)
