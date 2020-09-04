# https://www.acmicpc.net/problem/11576

from sys import stdin


def solution():
    A, B = map(int, stdin.readline().split())
    m = int(stdin.readline())
    A_list = list(map(int, stdin.readline().split()))
    answer = []
    total_sum = 0

    for i in range(len(A_list)):
        power = A ** (len(A_list) - (i + 1))
        total_sum += A_list[i] * power

    while total_sum:
        answer.append(total_sum % B)
        total_sum //= B

    print(*answer[::-1])


solution()
