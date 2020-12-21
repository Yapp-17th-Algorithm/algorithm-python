# https://www.acmicpc.net/problem/1744
# !!! 1과 x(x>0)는 곱하는 것보다 더하는게 더 큼 !!!

N = int(input())
plus, minus = [], []

for _ in range(N):
    n = int(input())
    if n > 0:
        plus.append(n)
    else:
        minus.append(n)
minus.sort()
plus.sort(reverse=True)
lm, lp = len(minus), len(plus)

ans = 0
for i in range(0, lp, 2):
    if lp % 2 and i+1 == lp:
        ans += plus[i]
    elif plus[i+1] == 1:
        ans += (plus[i] + plus[i+1])
    else:
        ans += (plus[i] * plus[i+1])

for i in range(0, lm, 2):
    if lm % 2 and i+1 == lm:
        ans += minus[i]
    else:
        ans += (minus[i] * minus[i+1])
print(ans)
