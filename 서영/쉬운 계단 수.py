# https://www.acmicpc.net/problem/10844
# dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

from sys import stdin

N = int(stdin.readline())
dp = [[0] * 12 for _ in range(N)]        # dp[i][j] : 길이가 i+1이고 1의 자리 숫자가 j-1인 계단수의 수
dp[0] = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

for i in range(1, N):
    for j in range(1, 11):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 10**9
print(sum(dp[-1]) % 10**9)
