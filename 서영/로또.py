# https://www.acmicpc.net/problem/6603

from sys import stdin
from itertools import combinations

while True:
    num = list(map(int, stdin.readline().split()))
    k = num[0]
    if k == 0:
        break
    for case in combinations(num[1:], 6):
        print(*case)
    print()