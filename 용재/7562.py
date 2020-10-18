# https://www.acmicpc.net/problem/7562
# 나이트의 이동

from collections import deque

def bfs(x: int, y: int, cx: int, cy: int) -> None:
  queue.append([x, y, 0])

  v = [[False] * size for _ in range(size)]
  v[y][x] = True

  while queue:
    tx, ty, tt = queue.popleft()

    if cx == tx and cy == ty:
      print(tt)
      break

    for i in range(8):
      if 0 <= tx + dx[i] < size and 0 <= ty + dy[i] < size and not v[ty + dy[i]][tx + dx[i]]:
        queue.append([tx + dx[i], ty + dy[i], tt + 1])
        v[ty + dy[i]][tx + dx[i]] = True

N = int(input())

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

for _ in range(N):
  queue = deque()

  size = int(input())
  x, y = [int(i) for i in input().split()]
  cx, cy = [int(i) for i in input().split()]

  bfs(x, y, cx, cy)
