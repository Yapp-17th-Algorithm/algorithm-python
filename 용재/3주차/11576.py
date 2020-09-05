# https://www.acmicpc.net/problem/11576
# Base Conversion

import math

A, B = map(int, input().split())

m = input()

Base = list(map(int, input().split()))

sum_of = 0

digit = 0

answer = []

for each in Base[::-1]:
  sum_of += each * (A ** digit)
  digit += 1

while sum_of:
  answer.append(sum_of % B)
  sum_of = math.floor((sum_of / B))

print(*answer[::-1])
