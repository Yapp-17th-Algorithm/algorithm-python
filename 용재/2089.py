# https://www.acmicpc.net/problem/2089
# -2진수

import math

N = int(input());

answer = ''

if not N:
  answer = '0'

while N:
  if N % -2:
    answer = '1' + answer
    N //= -2 + 1
  else:
    answer = '0' + answer
    N = math.floor(N / -2)

print(answer);
