# https://www.acmicpc.net/problem/11724

import sys
sys.setrecursionlimit(10 ** 6)


def dfs(x, edge, visited):
    visited[x] = True
    for next_target in edge[x]:
        if not visited[next_target]:
            dfs(next_target, edge, visited)


def solution():
    N, M = map(int, input().split())
    edge = [[] for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        edge[u].append(v)
        edge[v].append(u)

    ans = 0
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i, edge, visited)
            ans += 1
    print(ans)


solution()
