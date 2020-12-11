# https://www.acmicpc.net/problem/11047


def solution():
    N, K = map(int, input().split())
    answer = 0
    coins = [int(input()) for _ in range(N)]
    coins = coins[::-1]
    for coin in coins:
        if K == 0:
            break
        val = K // coin
        if K // coin > 0:
            answer += val
            K -= (val) * coin
    print(answer)


solution()
