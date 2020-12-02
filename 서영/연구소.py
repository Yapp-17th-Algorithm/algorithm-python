# https://www.acmicpc.net/problem/14502

from itertools import combinations
from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

virus = []
space = []
for i in range(N):
    for j in range(M):
        if map[i][j] == 2:
            virus.append((i, j))
        elif map[i][j] == 0:
            space.append((i, j))

ans = 0
for sp in combinations(space, 3):
    tmp = deepcopy(map)
    for i in range(3):
        tmp[sp[i][0]][sp[i][1]] = 1
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and not tmp[nx][ny]:
                tmp[nx][ny] = 2
                q.append((nx, ny))
    cnt = 0
    for row in tmp:
        cnt += row.count(0)
    ans = max(ans, cnt)

print(ans)
