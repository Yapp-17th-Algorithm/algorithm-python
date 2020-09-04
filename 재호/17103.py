# https://www.acmicpc.net/problem/17103

from sys import stdin


def get_prime_nums(max_n):
    prime_numbers = []
    pnum_check = [False for _ in range(max_n + 1)]

    for i in range(2, max_n + 1):
        if not pnum_check[i]:
            prime_numbers.append(i)
            for j in range(i * 2, max_n + 1, i):
                if not pnum_check[j]:
                    pnum_check[j] = True

    return prime_numbers, pnum_check


def solution():
    T = int(stdin.readline())
    max_n = 1000000
    prime_numbers, pnum_check = get_prime_nums(max_n)

    for _ in range(T):
        now = int(stdin.readline())
        cnt = 0
        for i in range(2, now // 2 + 1):
            if not pnum_check[i] and not pnum_check[now - i] and i + (now - i) == now:
                cnt += 1
        print(cnt)


solution()
