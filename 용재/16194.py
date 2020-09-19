# https://www.acmicpc.net/problem/16194
# 카드 구매하기 2

N  = int(input())

P = list(map(int, input().split()))

dp = [False] * (N + 1)

for i in range(1, N + 1):
  for j in range(1, i + 1):
    if dp[i]:
      dp[i] = min(dp[i], dp[i - j] + P[j - 1])
    else:
      dp[i] = dp[i - j] + P[j - 1]

print(dp[N])
