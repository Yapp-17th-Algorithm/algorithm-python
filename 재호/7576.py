# https://www.acmicpc.net/problem/7576

from collections import deque
from sys import stdin


def check_idx(y, x, N, M):
    return 0 <= y < N and 0 <= x < M


def go_days(warehouse, N, M, dq):
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    while dq:
        y, x = dq.popleft()
        for direction in directions:
            next_y, next_x = y + direction[0], x + direction[1]
            if check_idx(next_y, next_x, N, M) and warehouse[next_y][next_x] == 0:
                warehouse[next_y][next_x] = warehouse[y][x] + 1
                dq.append((next_y, next_x))
    
    for row in warehouse:
        if 0 in row:
            return -1
    
    return max(map(max, warehouse)) - 1


def solution():
    M, N = map(int, stdin.readline().split())
    warehouse = []
    dq = deque()

    for i in range(N):
        row = list(map(int, stdin.readline().split()))
        for j in range(M):
            if row[j] == 1:
                dq.append((i, j))
        warehouse.append(row)

    if not dq:
        print(-1)
        return
    
    print(go_days(warehouse, N, M, dq))


solution()
