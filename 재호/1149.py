# https://www.acmicpc.net/problem/1149

from sys import stdin


def solution():
    N = int(stdin.readline())
    arr, dp = [], [[0 for _ in range(3)] for __ in range(N)]
    for _ in range(N):
        arr.append(list(map(int, stdin.readline().split())))

    dp[0][0] = arr[0][0]
    dp[0][1] = arr[0][1]
    dp[0][2] = arr[0][2]
    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2]

    print(min(dp[N - 1]))


solution()
