import sys
sys.stdin = open("input.txt", "r")

n = int(input())

if n == 0:
  print(0)
  sys.exit(0)

result = ''

#  -13 = -2*(7) + 1
#   7  = -2*(-3) + 1
#  -3  = -2*(2) + 1
#   2  = -2*(-1) + 0
#  -1  = -2*(1) + 1
#   1  = -2*(0) + 1
# 출처: https://suri78.tistory.com/119 [공부노트]

while n:
  if n % -2:
    result = '1' + result
    n = n // -2 + 1
  else:
    result = '0' + result
    n = n // -2