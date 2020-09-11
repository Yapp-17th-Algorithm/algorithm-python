# https://www.acmicpc.net/problem/10844
# 쉬운 계단 수

N = int(input())

stairNum = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1, 10):
  stairNum[1][i] = 1

for i in range(2, N + 1):
  for j in range(10):
    if j == 0:
      stairNum[i][j] = stairNum[i - 1][1]
    elif j == 9:
      stairNum[i][j] = stairNum[i - 1][8]
    else:
      stairNum[i][j] = stairNum[i - 1][j - 1] + stairNum[i - 1][j + 1]

print(sum(stairNum[N]) % 1000000000)
