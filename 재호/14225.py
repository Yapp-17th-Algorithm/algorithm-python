# https://www.acmicpc.net/problem/14225

from sys import stdin
from itertools import combinations


def solution():
    answer = -1
    answer_dict = {}
    N = int(stdin.readline())
    S = list(map(int, stdin.readline().split()))
    for e in S:
        answer_dict[e] = True
    for i in range(2, N + 1):
        for comb_sum in list(map(sum, combinations(S, i))):
            answer_dict[comb_sum] = True
    max_val = max(answer_dict.keys())
    for i in range(1, max_val + 1):
        if i not in answer_dict:
            answer = i
            break
    if answer == -1:
        answer = max_val + 1
    print(answer)


solution()
