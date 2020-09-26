# https://www.acmicpc.net/problem/2309
# 일곱 난쟁이

from typing import List

n: List[int] = [int(input()) for i in range(9)]

sum_n: int = sum(n)

answer: List[int] = []
for i in range(8):
  for j in range(i + 1, 9):
    if (sum_n - (n[i] + n[j])) == 100:
      answer.append(n[i])
      answer.append(n[j])
      break

n.remove(answer[0])
n.remove(answer[1])

n.sort()

for i in range(7):
  print(n[i])
