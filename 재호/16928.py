# https://www.acmicpc.net/problem/16928

from sys import stdin
from collections import deque


def bfs(fast_road, cnt):
    dq = deque()
    dq.append(1)

    while dq:
        nx = dq.popleft()
        if cnt[100] != 0:
            break
        for i in range(1, 7):
            next_pos = nx + i
            if next_pos in fast_road:
                next_pos = fast_road[next_pos]
            if next_pos <= 100 and cnt[next_pos] == 0:
                dq.append(next_pos)
                cnt[next_pos] = cnt[nx] + 1


def solution():
    N, M = map(int, stdin.readline().split())
    fast_road = {}
    cnt = [0 for _ in range(101)]
    for _ in range(N + M):
        frm, to = map(int, stdin.readline().split())
        fast_road[frm] = to
    
    bfs(fast_road, cnt)
    print(cnt[100])


solution()
