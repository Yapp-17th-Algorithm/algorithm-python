# https://www.acmicpc.net/problem/16948

from sys import stdin
from collections import deque


def can_i_go(r, c, N):
    return 0 <= r < N and 0 <= c < N;


def bfs(m, r1, c1):
    dr = [-2, -2, 0, 0, 2, 2]
    dc = [-1, 1, -2, 2, -1, 1]
    dq = deque()
    dq.append((r1, c1))
    m[r1][c1] = 0
    while dq:
        nr, nc = dq.popleft()
        for i in range(6):
            next_r = nr + dr[i]
            next_c = nc + dc[i]
            if can_i_go(next_r, next_c, len(m)) and m[next_r][next_c] == -1:
                m[next_r][next_c] = m[nr][nc] + 1
                dq.append((next_r, next_c))


def solution():
    N = int(stdin.readline());
    r1, c1, r2, c2 = map(int, stdin.readline().split())
    m = [[-1] * N for _ in range(N)]
    bfs(m, r1, c1)
    print(m[r2][c2] if m[r2][c2] else -1)


solution()
