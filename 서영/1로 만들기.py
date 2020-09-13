# https://www.acmicpc.net/problem/1463
# 10->9->3->1
# 10->5->4->2->1

from sys import stdin

N = int(stdin.readline())
dp = [0] * (N + 1)    # dp[x] : x를 1로 만들 때, 연산 최소 횟수

for i in range(2, N+1):
    # 1을 빼는 연산 먼저 하고 생각
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
print(dp[-1])

