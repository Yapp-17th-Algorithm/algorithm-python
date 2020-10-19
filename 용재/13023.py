# https://www.acmicpc.net/problem/13023
# ABCDE

def dfs(vertex: int, depth: int) -> None:
    if depth == 4:
      print(1)
      exit()

    for each in node[vertex]:
      if not visited[each]:
          visited[each] = True
          dfs(each, depth + 1)
          visited[each] = False

N, M = map(int, input().split())

node = [[] for _ in range(N)]

visited = [False] * N

for _ in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)
