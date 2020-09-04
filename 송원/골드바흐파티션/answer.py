import sys
sys.stdin = open("input.txt", "r")

t = int(input())
cases = [ int(input()) for _ in range(t) ]

# 이런 방법이 있다고????
MAX = 1000000
check = [False, False] + [True] * (MAX-1)
primes = []
prime_count = 0

for i in range(1, MAX+1):
  if check[i]:
    primes.append(i)
    prime_count += 1
    for j in range(i*2, MAX+1, i):
      check[j] = False

for case in cases:
  count = 0
  for i in range(1, prime_count):
    if primes[i] <= case - primes[i]:
      if check[case - primes[i]] == True:
        count += 1
    else:
      break

  print(count)
