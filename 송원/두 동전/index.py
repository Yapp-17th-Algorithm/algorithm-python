import sys
from collections import deque
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
coins = []
board = []
for i in range(n):
  row = list(input())
  board.append(row)
  found = 0
  for j in range(m):
    if row[j] == 'o':
      found += 1
      coins.append((j, i))
      if found > 1:
        break

Q1 = deque()
Q2 = deque()
Q1.append(coins)
count = 0

def move_item(from_Q, to_Q):
  while from_Q:
    c1, c2 = from_Q.popleft()
    
    for dx, dy in (1,0), (0,1), (-1,0), (0,-1):
      drop_count = 0
      x1 = c1[0] + dx
      y1 = c1[1] + dy
      x2 = c2[0] + dx
      y2 = c2[1] + dy

      if (x1 < 0 or x1 >= m) or (y1 < 0 or y1 >= n):
        drop_count += 1

      if (x2 < 0 or x2 >= m) or (y2 < 0 or y2 >= n):
        drop_count += 1

      if drop_count == 1:
        print(count)
        sys.exit(0)

      elif drop_count == 2:
        continue
      
      elif drop_count == 0:
        positions = []

        if board[y1][x1] != '#':
          positions.append((x1, y1))
        else:
          positions.append((c1[0], c1[1]))

        if board[y2][x2] != '#':
          positions.append((x2, y2))
        else:
          positions.append((c2[0], c2[1]))

        if positions not in to_Q:
          to_Q.append(positions)

while Q1 or Q2:
  if count > 10:
    print(-1)
    sys.exit(0)

  count += 1

  if Q1:
    move_item(Q1, Q2)

  elif Q2:
    move_item(Q2, Q1)

# 아 -1 만들 수 있는 경우...
    