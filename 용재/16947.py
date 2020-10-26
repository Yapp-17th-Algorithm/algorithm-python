# https://www.acmicpc.net/problem/16947
# 서울 지하철 2호선

from sys import setrecursionlimit
from collections import deque
from typing import Deque

setrecursionlimit(1000000)

def dfs(vertex: int, edge: int) -> int:
    if(visited[vertex]):
      return vertex
    visited[vertex] = 1
    for each in node[vertex]:
      if each == edge:
        continue
      ret = dfs(each, vertex)
      if ret == -2:
        return -2
      if ret >= 0:
        visited[vertex] = 2
        if vertex == ret:
          return -2
        else:
          return ret
    return -1

def bfs(queue: Deque[int]) -> None:
    while queue:
        x = queue.popleft()
        for each in node[x]:
            if result[each] == -1:
                queue.append(each)
                result[each] = result[x] + 1

N = int(input())

node = [[] for _ in range(N)]

visited = [0] * N

for _ in range(N):
    u, v = map(int, input().split())
    v = v - 1
    u = u - 1
    node[u].append(v)
    node[v].append(u)

dfs(0, -1)

result = [0] * N

q = []

for i in range(N):
    if visited[i] == 2:
        result[i] = 0
        q.append(i)
    else:
        result[i] = -1

for each in q:
    bfs(deque([each]))

print(*result)
