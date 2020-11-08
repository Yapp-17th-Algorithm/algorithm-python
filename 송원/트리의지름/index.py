import sys
sys.stdin = open("input.txt", "r")

v = int(input())
tree = [[10001] * (v) for _ in range(v)]

for n in range(v):
  tree[n][n] = 0
  info = list(map(int, input().split()))
  node = info[0]
  for i in range(1, len(info), 2):
    if info[i] != -1:
      tree[node - 1][info[i] - 1] = info[i + 1]

for k in range(v):
  for i in range(v):
    for j in range(v):
      if tree[i][j] > tree[i][k] + tree[k][j]:
        tree[i][j] = tree[i][k] + tree[k][j]

result = 0

for i in range(v):
  max_distance = max(tree[i])
  if result < max_distance:
    result = max_distance

print(result)