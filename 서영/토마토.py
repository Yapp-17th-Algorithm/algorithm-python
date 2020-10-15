# https://www.acmicpc.net/problem/7576

from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

tomato = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            tomato.append((i, j))

ans = 0
while tomato:
    ans += 1
    tom = tomato.copy()
    while tom:
        x, y = tom.popleft()
        tomato.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            if 0 <= x+dx < N and 0 <= y+dy < M:
                if box[x+dx][y+dy] == 0:
                    box[x+dx][y+dy] = 1
                    tomato.append((x+dx, y+dy))

print(-1 if any(0 in row for row in box) else ans-1)
