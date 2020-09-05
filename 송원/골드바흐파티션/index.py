import sys
sys.stdin = open("input.txt", "r")

t = int(input())
cases = [ int(input()) for _ in range(t) ]

def isPrime(num):
  result = True
  for i in range(2, num):
    if num % i == 0:
      result = False
      break
  return result

for case in cases:
  # 각 케이스마다 소수 리스트 생성
  primes = []
  for i in range(2, case // 2 + 1):
    if isPrime(i):
      primes.append(i)

  count = 0
  for i in primes:
    if i <= case - i:
      if isPrime(i):
        if isPrime(case - i):
          count += 1
    else:
      break

  print(count)

# 아 전체를 순회하는게 아니라 case 보다 작은 소수 리스트를 순회하도록 바꿔야 함
