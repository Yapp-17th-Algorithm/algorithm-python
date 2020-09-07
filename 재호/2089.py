# https://www.acmicpc.net/problem/2089

from sys import stdin


def solution():
    N = int(stdin.readline())
    answer = []
    if not N:
        print(0)
        return

    while N:
        answer.append(abs(N % -2))
        N //= -2
        if answer[-1]:
            N += 1
    answer.reverse()
    print(''.join([str(x) for x in answer]))


solution()
