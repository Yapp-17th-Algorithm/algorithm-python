import sys
from collections import deque
sys.stdin = open("input.txt", "r")

n = int(input())
graph = [ list(map(int, list(input()))) for _ in range(n)]
houses = []
Q = deque()

for i in range(n):
  for j in range(n):
    if graph[j][i] == 1:
      Q.append((i, j))
      graph[j][i] = 2
      count = 1
      while Q:
        pos_x, pos_y = Q.popleft()
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
          x = pos_x + dx
          y = pos_y + dy
          if 0 <= x <= n - 1 and 0 <= y <= n - 1 and graph[y][x] == 1:
            count += 1
            graph[y][x] = 2
            Q.append((x, y))

      houses.append(count)

print(len(houses))
houses.sort()
for i in houses:
  print(i)