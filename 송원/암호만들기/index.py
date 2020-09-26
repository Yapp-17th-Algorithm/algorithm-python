import sys
from itertools import combinations
sys.stdin = open("input.txt", "r")

L, C = map(int, input().split())
chars = input().split()
chars.sort()
vowels = []
consonants = []
results = []

for i in range(len(chars)):
  if chars[i] in ("a", "e", "i", "o", "u"):
    vowels.append(chars[i])
  else:
    consonants.append(chars[i])

count = 1
while count < L - 1:
  consonantCombinations = combinations(consonants, L - count)
  for consonantComb in consonantCombinations:
    vowelCombinations = combinations(vowels, count)
    for vowelComb in vowelCombinations:
      result = list(vowelComb) + list(consonantComb)
      result.sort()
      results.append("".join(result))
  count += 1

results.sort()
for result in results:
  print(result)