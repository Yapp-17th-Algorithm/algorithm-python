# https://www.acmicpc.net/problem/7562

from sys import stdin
from collections import deque


def check_idx(y, x, l):
    return 0 <= y < l and 0 <= x < l


def bfs(y, x, dest_y, dest_x, pan, l):
    dq = deque()
    dq.append((y, x))
    directions = [[-1, 2], [-2, 1], [-2, -1], [-1, -2], 
                 [1, -2], [2, -1], [2, 1], [1, 2]]
    while dq:
        now_y, now_x = dq.popleft()
        if now_y == dest_y and now_x == dest_x:
            return pan[now_y][now_x]
        for direction in directions:
            ny, nx = now_y + direction[0], now_x + direction[1]
            if check_idx(ny, nx, l) and pan[ny][nx] == 0:
                pan[ny][nx] = pan[now_y][now_x] + 1
                dq.append((ny, nx))


def solution():
    N = int(stdin.readline())
    for _ in range(N):
        l = int(stdin.readline()) # 체스판 l x l
        y, x = map(int, stdin.readline().split())
        dest_y, dest_x = map(int, stdin.readline().split())
        pan = [[0] * l for _ in range(l)]
        print(bfs(y, x, dest_y, dest_x, pan, l))


solution()
