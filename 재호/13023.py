# https://www.acmicpc.net/problem/13023

from sys import stdin, exit


def dfs(start, f, v, cnt):
    if cnt == 4:
        print(1)
        exit()
    v[start] = True
    for i in range(len(f[start])):
        if not v[f[start][i]]:
            dfs(f[start][i], f, v, cnt + 1)
    v[start] = False


def solution():
    N, M = map(int, stdin.readline().split())
    f = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, stdin.readline().split())
        f[a].append(b)
        f[b].append(a)

    v = [False for _ in range(N)]
    for i in range(N):
        dfs(i, f, v, 0)

    print(0)


solution()