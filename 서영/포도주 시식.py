# https://www.acmicpc.net/problem/2156
# dp[i] : i번째까지 마셨을 때 최대 포도주의 양
# [6, 16, 23, 28, 33, 33]

from sys import stdin

N = int(stdin.readline())
P = [int(stdin.readline()) for _ in range(N)]

dp = [0, P[0]]
if N > 1:
    dp.append(P[0]+P[1])
for i in range(3, N+1):
    dp.append(max(dp[i-1], dp[i-2] + P[i-1], dp[i-3] + P[i-2] + P[i-1]))
print(max(dp))
