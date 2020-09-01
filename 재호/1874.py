# https://www.acmicpc.net/problem/1874

from collections import deque
from sys import stdin


def solution():
    n = int(stdin.readline())
    stk = deque([x + 1 for x in range(n)])
    nums = [int(stdin.readline()) for _ in range(n)]
    solving_stk, answer = [], []

    for i in range(n):
        while stk and stk[0] <= nums[i]:
            solving_stk.append(stk.popleft())
            answer.append("+")
        if solving_stk and nums[i] == solving_stk[-1]:
            solving_stk.pop()
            answer.append("-")
        else:
            print("NO")
            return

    for a in answer:
        print(a)


solution()
