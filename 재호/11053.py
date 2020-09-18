# https://www.acmicpc.net/problem/11053

from sys import stdin


def solution():
    N = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))
    dp = [1 for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if A[i] > A[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    print(max(dp))


solution()
