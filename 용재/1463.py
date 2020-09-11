# https://www.acmicpc.net/problem/1463
# 1로 만들기

N = int(input())

check = [0] * (N + 1)

for i in range(2, N + 1):
  check[i] = check[i - 1] + 1
  if i % 2 == 0 and check[i // 2] + 1 < check[i]:
    check[i] = check[i // 2] + 1
  if i % 3 == 0 and check[i // 3] + 1 < check[i]:
    check[i] = check[i // 3] + 1

print(check[-1])
