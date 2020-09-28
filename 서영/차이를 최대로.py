# https://www.acmicpc.net/problem/10819

from sys import stdin
from itertools import permutations


N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

ans = 0
for case in permutations(A):
    tmp = sum(abs(case[i] - case[i+1]) for i in range(N-1))
    ans = max(ans, tmp)

print(ans)