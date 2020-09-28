import sys
from itertools import permutations
sys.stdin = open("input.txt", "r")

n = int(input())
numbers = list(map(int, input().split()))
maxValue = 0

def sumBetween(arr):
  sum = 0
  for i in range(len(arr) - 1):
    sum += abs(arr[i] - arr[i + 1])
  return sum

for arranged in permutations(numbers, len(numbers)):
  sumBetweenValue = sumBetween(arranged)
  if sumBetweenValue > maxValue:
    maxValue = sumBetweenValue

print(maxValue)