# https://www.acmicpc.net/problem/10819

from sys import stdin


def next_permutation(perm):
    n = len(perm)
    i = n - 1
    while i > 0 and perm[i - 1] >= perm[i]:
        i -= 1

    if i <= 0:
        return False

    j = n - 1
    while perm[j] <= perm[i - 1]:
        j -= 1
    perm[i - 1], perm[j] = perm[j], perm[i - 1]

    k = n - 1
    while i < k:
        perm[i], perm[k] = perm[k], perm[i]
        i += 1
        k -= 1

    return True


def calc(l):
    ans = 0
    for i in range(len(l) - 1):
        ans += abs(l[i] - l[i + 1])
    return ans


def solution():
    ans = 0
    N = int(stdin.readline())
    l = list(map(int, stdin.readline().split()))
    l.sort()

    while next_permutation(l):
        ans = max(ans, calc(l))

    print(ans)


solution()
