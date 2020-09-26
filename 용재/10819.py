# https://www.acmicpc.net/problem/10819
# 차이를 최대로

from itertools import permutations
from typing import List

N: int = int(input())

numbers: List[int] = list(map(int, input().split()))

numbers_permutation = permutations(numbers)

answer = 0

for each in numbers_permutation:
  calc = 0
  for i in range(N-1):
    calc += abs(each[i] - each[i + 1])

  answer = max(answer, calc)

print(answer)
