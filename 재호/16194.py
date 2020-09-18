# https://www.acmicpc.net/problem/16194

from sys import stdin


def solution():
    N = int(stdin.readline())
    INF = 10 ** 9
    dp = [INF for _ in range(N + 1)]
    dp[0] = 0
    P = list(map(int, stdin.readline().split()))
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            if dp[i] > dp[i - j] + P[j - 1]:
                dp[i] = dp[i - j] + P[j - 1]
    print(dp[N])


solution()
