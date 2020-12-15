# https://www.acmicpc.net/problem/11047
# 동전 0

N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]

coin_count = 0

for i in range(1, N + 1):
    coin = coins[-i]

    if K >= coin:
        num = K // coin
        K -= coin * num

        coin_count += num

print(coin_count)