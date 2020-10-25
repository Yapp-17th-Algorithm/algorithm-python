# https://www.acmicpc.net/problem/2667

from sys import stdin
from collections import deque


def bfs(tx, ty):
    cnt = 0
    queue = deque([(tx, ty)])
    while queue:
        cnt += 1
        x, y = queue.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            if 0 <= x+dx < N and 0 <= y+dy < N and map[x+dx][y+dy] and not visit[x+dx][y+dy]:
                visit[x+dx][y+dy] = True
                queue.append((x+dx, y+dy))
    return cnt


N = int(stdin.readline())
map = [list(map(int, list(stdin.readline().rstrip()))) for _ in range(N)]
visit = [[False] * N for _ in range(N)]
ans = []

for i in range(N):
    for j in range(N):
        if map[i][j] and not visit[i][j]:
            visit[i][j] = True
            ans.append(bfs(i, j))

print(len(ans))
for a in sorted(ans):
    print(a)
