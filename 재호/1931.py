# https://www.acmicpc.net/problem/1931


def solution():
    N = int(input())
    intervals = sorted([list(map(int, input().split()))
                        for _ in range(N)], key=lambda x: (x[1], x[0]))
    answer = last = 0
    for interval in intervals:
        if last <= interval[0]:
            last = interval[1]
            answer += 1
    print(answer)


solution()
