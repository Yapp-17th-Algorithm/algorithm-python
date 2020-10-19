import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
check = [0] * n
arranged = {}

if m < 4:
  print(0)
  sys.exit(0)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

def DFS(index, count):
  if count >= 4:
    print(1)
    sys.exit(0)
  
  for i in range(len(graph[index])):
    if check[i] != 1 and graph[index][i] == 1:
      check[i] = 1
      DFS(i, count + 1)
      check[i] = 0

for j in range(n):
  check[j] = 1
  DFS(j, 0)
  check[j] = 0

print(0)