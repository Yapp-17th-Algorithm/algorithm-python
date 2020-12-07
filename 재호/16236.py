# https://www.acmicpc.net/problem/16236

from sys import stdin
from collections import deque


def can_i_go(m, y, x, size, N):
    return 0 <= y < N and 0 <= x < N and m[y][x] <= size


def bfs(start_y, start_x, m, size, N):
    v = [[-1] * N for _ in range(N)]
    dq = deque()
    dq.append((start_y, start_x))
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    v[start_y][start_x] = 0
    can_eat = []
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if can_i_go(m, ny, nx, size, N) and v[ny][nx] == -1:
                v[ny][nx] = v[y][x] + 1
                dq.append([ny, nx])
                if 1 <= m[ny][nx] < size:
                    can_eat.append((ny, nx, v[ny][nx]))
    can_eat = sorted(can_eat, key=lambda x: (x[2], x[0], x[1]))
    return can_eat[0] if can_eat else []


def solution():
    N = int(stdin.readline())
    m = [list(map(int, stdin.readline().split())) for _ in range(N)]
    now = [0, 0]
    size = 2
    answer = ate_cnt = 0
    for i in range(N):
        for j in range(N):
            if m[i][j] == 9:
                now[0] = i
                now[1] = j
                m[i][j] = 0
                break

    while True:
        res = bfs(now[0], now[1], m, size, N)
        if res:
            ate_cnt += 1
            answer += res[2]
            now[0] = res[0]
            now[1] = res[1]
            m[now[0]][now[1]] = 0
            if ate_cnt == size:
                size += 1
                ate_cnt = 0
        else:
            break
    print(answer)


solution()
