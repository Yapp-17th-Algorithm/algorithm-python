# https://www.acmicpc.net/problem/2156
# 포도주 시식

n = int(input())

glasses = [int(input()) for _ in range(n)]

dp = [0] * n

if n == 1:
  print(glasses[0])
if n == 2:
  print(glasses[0] + glasses[1])
if n > 2:
  dp[0] = glasses[0]
  dp[1] = dp[0] + glasses[1]
  dp[2]=max(dp[1], dp[0] + glasses[2], glasses[1] + glasses[2])

  for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-2] + glasses[i], dp[i-3] + glasses[i] + glasses[i-1])

  print(dp[n-1])
