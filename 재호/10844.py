# https://www.acmicpc.net/problem/10844

from sys import stdin


def solution():
    N = int(stdin.readline())
    dp = [[0 for _ in range(10)] for __ in range(N)]
    dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for i in range(1, N):
        for j in range(10):
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]
            if j < 9:
                dp[i][j] += dp[i - 1][j + 1]
    print(sum(dp[N - 1]) % 1000000000)


solution()
