# https://www.acmicpc.net/problem/2448
# 별 찍기 11

import math
from sys import stdin, setrecursionlimit

def star(x: int, y: int, n:int) -> None:
    if n == 3:
        # 1
        arr[y][x] = '*'

        # 2
        arr[y + 1][x - 1] = '*'
        arr[y + 1][x + 1] = '*'

        # 3
        for i in range(5):
            arr[y + 2][x - 2 + i] = '*'

    else:
        calc_n = n // 2
        star(x, y, calc_n)
        star(x - calc_n, y + calc_n, calc_n)
        star(x + calc_n, y + calc_n, calc_n)

n = int(stdin.readline())

arr = [[' '] * n * 2 for _ in range(n)]

star(n - 1, 0, n)

for each in arr:
    print(''.join(each))
