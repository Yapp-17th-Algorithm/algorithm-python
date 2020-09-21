# https://www.acmicpc.net/problem/2156

from sys import stdin


def solution():
    N = int(stdin.readline())
    amount = []
    dp = [0 for _ in range(N)]
    for _ in range(N):
        amount.append(int(stdin.readline()))
    dp[0] = amount[0]
    if N >= 2:
        dp[1] = dp[0] + amount[1]
    if N >= 3:
        dp[2] = max(dp[1], dp[0] + amount[2], amount[1] + amount[2])
    if N >= 4:
        for i in range(3, N):
            dp[i] = max(dp[i - 1],
                        dp[i - 2] + amount[i],
                        dp[i - 3] + amount[i - 1] + amount[i])

    print(dp[N - 1])


solution()
