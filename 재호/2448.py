# https://www.acmicpc.net/problem/2448

import math


def make(stars, push_cnt):
    l = len(stars)
    for i in range(l):
        stars.append(stars[i] + stars[i])
        stars[i] = ("   " * push_cnt) + stars[i] + ("   " * push_cnt)


def solution():
    N = int(input())
    stars = ["  *   ", " * *  ", "***** "]
    for i in range(int(math.log2(N // 3))):
        make(stars, 2 ** i)

    print("\n".join(stars))


solution()
