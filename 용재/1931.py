# https://www.acmicpc.net/problem/1931
# 회의실배정

from sys import stdin

N = int(stdin.readline())

schedule = [[0] * 2 for _ in range(N)]

for i in range(N):
    start, end = map(int, stdin.readline().split())
    schedule[i][0] = start
    schedule[i][1] = end

schedule.sort(key = lambda x: (x[1], x[0]))

count = 0
end_time = 0

for i, j in schedule:
    if i >= end_time:
        count += 1
        end_time = j

print(count)
