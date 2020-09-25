# https://www.acmicpc.net/problem/1759

from sys import stdin


def check(password):
    mo, ja = 0, 0
    for p in password:
        if p == 'a' or p == 'e' or p == 'i' or p == 'o' or p == 'u':
            mo += 1
        else:
            ja += 1
    return mo >= 1 and ja >= 2


def go(L, alpha, password, i):
    if len(password) == L and check(password):
        print(password)
        return
    if i < len(alpha):
        go(L, alpha, password + alpha[i], i + 1)
        go(L, alpha, password, i + 1)


def solution():
    L, C = map(int, stdin.readline().split())
    alpha = stdin.readline().split()
    alpha.sort()
    go(L, alpha, "", 0)


solution()
