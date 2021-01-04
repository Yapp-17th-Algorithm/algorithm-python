# https://www.acmicpc.net/problem/1780

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


def check_is_same_area(start_y, start_x, end_y, end_x, matrix):
    start = matrix[start_y][start_x]
    for i in range(start_y, end_y + 1):
        for j in range(start_x, end_x + 1):
            if start != matrix[i][j]:
                return False
    return True


def check_can_slice(start_y, start_x, end_y, end_x, answer, matrix):
    now_n = (end_y - start_y) + 1
    if check_is_same_area(start_y, start_x, end_y, end_x, matrix):
        answer[matrix[start_y][start_x] + 1] += 1
        return

    new_n = now_n // 3
    for i in range(3):
        for j in range(3):
            check_can_slice(i * new_n + start_y, j * new_n + start_x, ((i + 1) * new_n) - 1 + start_y,
                            ((j + 1) * new_n) - 1 + start_x, answer, matrix)


def solution():
    answer = [0, 0, 0]
    N = int(stdin.readline())
    matrix = [list(map(int, stdin.readline().split())) for _ in range(N)]
    check_can_slice(0, 0, N - 1, N - 1, answer, matrix)
    for a in answer:
        print(a)


solution()
