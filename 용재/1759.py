# https://www.acmicpc.net/problem/1759
# 암호 만들기

from typing import List, Set
from itertools import combinations

vowels: List[str] = list("aeiou")

L, C = map(int, input().split())

each_alphabets: List[str] = sorted(list(map(str, input().split())))

vowels_in: Set[str] = set(each_alphabets) & set(vowels)

for each in combinations(each_alphabets, L):
  num: int = len(set(each) & vowels_in)
  if num == 0 or L - num < 2:
    continue
  print(''.join(each))
