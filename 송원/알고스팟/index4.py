import sys
import heapq as hq
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(m)]
crash = [[1000000] * n for _ in range(m)]
crash[0][0] = 0
h = []
hq.heappush(h, (0, (0, 0)))

while h:
  count, (pos_x, pos_y) = hq.heappop(h)
  if pos_x == n - 1 and pos_y == m - 1:
    break
  
  for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
    x = pos_x + dx
    y = pos_y + dy
    if 0 <= x <= n - 1 and 0 <= y <= m - 1:
      new_crash = 0
      if graph[y][x] == 1:
        new_crash = count + 1
      else:
        new_crash = count
      if crash[y][x] > new_crash:
        crash[y][x] = new_crash
        hq.heappush(h, (new_crash, (x, y)))

print(crash[m - 1][n - 1])
