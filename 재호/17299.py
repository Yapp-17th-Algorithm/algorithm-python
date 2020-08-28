# https://www.acmicpc.net/problem/17299

from sys import stdin


def solution():
    N = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))
    F = [0] * ((10 ** 6) + 1)
    answer = [0] * (10 ** 6)
    stk = []

    for x in A:
        F[x] += 1

    stk.append(0)
    for i in range(1, len(A)):
        while stk and F[A[stk[-1]]] < F[A[i]]:
            answer[stk.pop()] = A[i]
        stk.append(i)

    while stk:
        answer[stk.pop()] = -1

    print(" ".join([str(answer[i]) for i in range(N)]))


solution()
