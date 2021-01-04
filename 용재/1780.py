# https://www.acmicpc.net/problem/1780
# 종이의 개수

from sys import stdin

def inner_divide(x: int, y: int, n: int) -> None:
    for i in range(3):
        for j in range(3):
            calc_n = n // 3
            divide(x + i * calc_n, y + j * calc_n, calc_n)


def divide(x: int, y: int, n: int) -> None:
    global count_result

    standard = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if standard != paper[i][j]:
                inner_divide(x, y, n)
                return

    if standard == -1:
        count_result[0] += 1
    elif standard == 0:
        count_result[1] += 1
    elif standard == 1:
        count_result[2] += 1


n = int(stdin.readline())
paper = [list(map(int, stdin.readline().split())) for _ in range(n)]

count_result = [0, 0, 0] # -1, 0, 1

divide(0, 0, n)

for each in count_result:
    print(each)
