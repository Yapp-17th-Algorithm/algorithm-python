import sys
sys.setrecursionlimit(1000000000) 
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visits = [0] * (n + 1)
visits[0] = -1
count = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def visit(node):
  if visits[node] == 0:
    visits[node] = 1
    for n in graph[node]:
      if visits[n] == 0:
        visit(n)
  else:
    return


for i in range(1, n + 1):
  if visits[i] == 0:
    count += 1
    visit(i)

print(count)