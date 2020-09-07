# https://www.acmicpc.net/problem/17103
# 골드바흐 파티션

import math

count = 1000001
primes = [False, False] + [True] * (count - 1)

for i in range(2, count + 1):
  if primes[i]:
    for j in range(2 * i, count + 1, i):
        primes[j] = False

T = int(input())

N = [int(input()) for _ in range(T)]

for each in N:
  answer = 0
  for i in range(2, each // 2 + 1):
    if primes[i] and primes[each - i]:
      answer += 1

  print(answer)
