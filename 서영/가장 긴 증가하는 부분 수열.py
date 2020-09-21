# https://www.acmicpc.net/problem/11053
# dp[i] : i 포함? / 안포함? => 포함인듯
# [1,2,1,3,2,4] / [1,2,2,3,3,4]

from sys import stdin

N = int(stdin.readline())
L = list(map(int, stdin.readline().split()))

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if L[i] > L[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(max(dp))
