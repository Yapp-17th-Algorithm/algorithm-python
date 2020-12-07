# https://www.acmicpc.net/problem/14502

from sys import stdin
from collections import deque


def can_i_go(m, y, x, N, M):
    return 0 <= y < N and 0 <= x < M and m[y][x] == 0


def bfs(m, viruses, N, M):
    dq = deque(viruses)
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if can_i_go(m, ny, nx, N, M):
                m[ny][nx] = 2
                dq.append([ny, nx])


def solution():
    N, M = map(int, stdin.readline().split())
    m = [list(map(int, stdin.readline().split())) for _ in range(N)]
    answer = -1

    viruses = []
    for i in range(N):
        for j in range(M):
            if m[i][j] == 2:
                viruses.append([i, j])
    
    for w1 in range((N * M) - 2):
        w1y = w1 // M
        w1x = w1 % M
        if not can_i_go(m, w1y, w1x, N, M):
            continue
        for w2 in range(w1 + 1, (N * M) - 1):
            w2y = w2 // M
            w2x = w2 % M
            if not can_i_go(m, w2y, w2x, N, M):
                continue
            for w3 in range(w2 + 1, N * M):
                w3y = w3 // M
                w3x = w3 % M
                if not can_i_go(m, w3y, w3x, N, M):
                    continue
                new_m = [row[:] for row in m]
                new_m[w1y][w1x] = 1
                new_m[w2y][w2x] = 1
                new_m[w3y][w3x] = 1
                bfs(new_m, viruses, N, M)
                safe_count = sum([x.count(0) for x in new_m])
                if answer < safe_count:
                    answer = safe_count
    
    print(answer)


solution()
