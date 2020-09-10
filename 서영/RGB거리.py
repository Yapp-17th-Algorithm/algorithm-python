# https://www.acmicpc.net/problem/1149

from sys import stdin

N = int(stdin.readline())
cost = [list(map(int, stdin.readline().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(3):
        cost[i][j] += min(cost[i-1][:j] + cost[i-1][j+1:])

print(min(cost[-1]))