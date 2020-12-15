# https://www.acmicpc.net/problem/11047


N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

cnt = 0
for x in reversed(coins):
    cnt += K // x
    K %= x
print(cnt)