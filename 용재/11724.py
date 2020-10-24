# https://www.acmicpc.net/problem/11724
# 연결 요소의 개수

def dfs(vertex: int) -> None:
    visited[vertex] = True
    for i in node[vertex]:
         if visited[i] == False:
             dfs(i)

N, M = map(int, input().split())

node = [[] for _ in range(N)]

visited = [False] * (N)

for _ in range(M):
    u, v = map(int, input().split())
    u = u - 1
    v = v - 1
    node[u].append(v)
    node[v].append(u)

count = 0

for i in range(N):
    if visited[i] == False:
        dfs(i)
        count += 1

print(count)
