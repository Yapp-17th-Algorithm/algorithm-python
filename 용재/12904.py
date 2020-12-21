# https://www.acmicpc.net/problem/12904
# A와 B

from sys import stdin

S = list(stdin.readline().strip())
T = list(stdin.readline().strip())

while len(S) != len(T):
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T = T[::-1]

if S == T:
    print(1)
else:
    print(0)
