import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
friends = [[] * n for _ in range(n)]
check = [0] * n

if m < 4:
  print(0)
  sys.exit(0)

for _ in range(m):
  a, b = map(int, input().split())
  friends[a].append(b)
  friends[b].append(a)

def DFS(index, count):
  if count >= 4:
    print(1)
    sys.exit(0)
  
  for friend in friends[index]:
    if check[friend] != 1:
      check[friend] = 1
      DFS(friend, count + 1)
      check[friend] = 0

for j in range(n):
  check[j] = 1
  DFS(j, 0)
  check[j] = 0

print(0)