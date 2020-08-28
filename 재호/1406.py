# https://www.acmicpc.net/problem/1406

def solution():
    stk1, stk2 = [], []
    string = input()
    for c in string:
        stk1.append(c)
    M = int(input())
    for _ in range(M):
        op = list(map(str, input().split()))
        if op[0] == 'L' and stk1:
            stk2.append(stk1.pop())
        elif op[0] == 'D' and stk2:
            stk1.append(stk2.pop())
        elif op[0] == 'B' and stk1:
            stk1.pop()
        elif op[0] == 'P':
            stk1.append(op[1])
    while stk1:
        stk2.append(stk1.pop())
    while stk2:
        print(stk2.pop(), end='')


solution()
