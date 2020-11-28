# https://www.acmicpc.net/problem/14888


def div_method(a, b):
    if a > 0:
        return a // b
    else:
        return -(-a // b)


def go(a, idx, cur, plus, minus, mul, div):
    res = []
    if idx == len(a):
        return (cur, cur)
    if plus > 0:
        res.append(go(a, idx + 1, cur + a[idx], plus - 1, minus, mul, div))
    if minus > 0:
        res.append(go(a, idx + 1, cur - a[idx], plus, minus - 1, mul, div))
    if mul > 0:
        res.append(go(a, idx + 1, cur * a[idx], plus, minus, mul - 1, div))
    if div > 0:
        res.append(go(a, idx + 1, div_method(cur, a[idx]), plus, minus, mul, div - 1))
    return max([t[0] for t in res]), min([t[1] for t in res])


def solution():
    N = int(input())
    a = list(map(int, input().split()))
    PLUS, MINUS, MUL, DIV = map(int, input().split())
    ans = go(a, 1, a[0], PLUS, MINUS, MUL, DIV)
    print(ans[0])
    print(ans[1])


solution()
