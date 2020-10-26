# https://www.acmicpc.net/problem/16947

from sys import stdin, setrecursionlimit
from collections import deque

setrecursionlimit(10 ** 6)

def init_visited(v):
    for i in range(len(v)):
        v[i] = False


def dfs(start, now, cnt, edges, visited, cycle):
    visited[now] = True
    for edge in edges[now]:
        if not visited[edge]:
            dfs(start, edge, cnt + 1, edges, visited, cycle)
        elif start == edge and cnt >= 2:
            cycle[edge] = True
            return


def bfs(start, edges, cycle, visited):
    init_visited(visited)
    dq = deque()
    dq.append((start, 0))
    while dq:
        now, now_cnt = dq.popleft()
        if cycle[now]:
            return now_cnt
        for edge in edges[now]:
            if not visited[edge]:
                visited[edge] = True
                dq.append((edge, now_cnt + 1))


def solution():
    N = int(stdin.readline())
    edges = [[] for _ in range(N + 1)]
    cycle = [False] * (N + 1);
    visited = [False] * (N + 1);

    for _ in range(N):
        a, b = map(int, stdin.readline().split())
        edges[a].append(b)
        edges[b].append(a)

    for i in range(1, N + 1):
        init_visited(visited)
        dfs(i, i, 0, edges, visited, cycle)

    print(*[bfs(x, edges, cycle, visited) if not cycle[x] else 0 for x in range(1, N + 1)])


solution()
