import sys
from collections import deque
sys.stdin = open("input.txt", "r")

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [0] * (n + 1)
result = []

def DFS(node, prev):
  visited[node] = 1
  found = False
  for i in graph[node]:
    if visited[i] == 0:
      DFS(i, node)
      if visited[i] == 2:
        visited_count = 0
        for j in graph[i]:
          if visited[j] == 2:
            visited_count += 1
        if visited_count < 2:
          visited[node] = 2
    elif visited[i] == 1 and i != prev and prev != 0:
      visited[i] = 2
      visited[node] = 2
      found = True
  if found:
    return True
  else:
    return False
  
  return False

DFS(1, 0)

# 이제 이 아래가 문제군

for node in range(1, n + 1):
  if visited[node] == 2:
    result.append('0')
    continue

  Q = deque()
  Q.append(node)
  visited2 = [0] * (n + 1)
  visited2[node] = 1
  count = 0
  found = False 

  while Q and not found:
    count += 1
    toward = Q.popleft()

    for i in graph[toward]:
      if visited[i] != 2 and visited2[i] == 0:
        visited2[1] = 1
        Q.append(i)

      elif visited[i] == 2:
        found = True
        break
  
  result.append(str(count))

print(' '.join(result))