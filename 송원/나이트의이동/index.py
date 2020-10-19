import sys
sys.stdin = open("input.txt", "r")
from collections import deque

n = int(input())
dx = [-2, -1, -2, -1, 2, 1, 2, 1]
dy = [-1, -2, 1, 2, -1, -2, 1, 2]

for _ in range(n):
  Q = deque()
  I = int(input())
  board = [[0] * I for _ in range(I)]
  distance = [[0] * I for _ in range(I)]
  start_x, start_y = map(int, input().split())
  dest_x, dest_y = map(int, input().split())
  Q.append((start_x, start_y))
  board[start_y][start_x] = 1
  while board[dest_y][dest_x] != 1:
    prev_x, prev_y = Q.popleft()
    for i in range(8):
      x = prev_x + dx[i]
      y = prev_y + dy[i]
      if 0 <= x <= I - 1 and 0 <= y <= I -1 and board[y][x] != 1:
        board[y][x] = 1
        distance[y][x] = distance[prev_y][prev_x] + 1
        Q.append((x, y))

  print(distance[dest_y][dest_x])