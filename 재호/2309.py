# https://www.acmicpc.net/problem/2309

from sys import stdin


def find_lier(total, smalls):
    for i in range(len(smalls) - 1):
        for j in range(i + 1, len(smalls)):
            if total - (smalls[i] + smalls[j]) == 100:
                return [smalls[i], smalls[j]]


def solution():
    smalls = [int(stdin.readline()) for _ in range(9)]
    smalls.sort()
    total = sum(smalls)
    lier_list = find_lier(total, smalls)
    for small in smalls:
        if small not in lier_list:
            print(small)


solution()
