# https://www.acmicpc.net/problem/1149
# RGB 거리

N = int(input())

inputColors = [list(map(int, input().split())) for _ in range(N)]

colorSum = [[0] * 3 for _ in range(N)]

for i, each in enumerate(inputColors):
  colorSum[i][0] = each[0] + min(colorSum[i - 1][1], colorSum[i - 1][2])
  colorSum[i][1] = each[1] + min(colorSum[i - 1][0], colorSum[i - 1][2])
  colorSum[i][2] = each[2] + min(colorSum[i - 1][0], colorSum[i - 1][1])

print(min(colorSum[N - 1]))
