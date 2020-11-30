# https://www.acmicpc.net/problem/1963

from sys import stdin
from collections import deque


def eratos(eratos_list):
    eratos_list[0] = eratos_list[1] = False
    for i in range(2, 10000):
        if not eratos_list[i]:
            continue
        for j in range(i + i, 10000, i):
            if eratos_list[j]:
                eratos_list[j] = False


def bfs(t1, cnt, eratos_list):
    dq = deque()
    dq.append(t1)
    while dq:
        now_num = dq.popleft()
        for i in range(4):
            for j in range(10):
                now_temp_num = [x for x in str(now_num)]
                now_temp_num[i] = str(j)
                now_temp_num = int("".join(now_temp_num))

                if now_temp_num >= 10000 or now_temp_num < 1000 or now_num == now_temp_num:
                    continue

                if eratos_list[now_temp_num] and cnt[now_temp_num] == 0:
                    dq.append(now_temp_num)
                    cnt[now_temp_num] = cnt[now_num] + 1


def solution():
    T = int(stdin.readline())
    eratos_list = [True for _ in range(10000)]
    eratos(eratos_list)
    for _ in range(T):
        t1, t2 = map(int, stdin.readline().split())
        if t1 == t2:
            print(0)
            continue
        cnt = [0 for _ in range(10000)]
        bfs(t1, cnt, eratos_list)
        print(cnt[t2] if cnt[t2] != 0 else "Impossible")


solution()
