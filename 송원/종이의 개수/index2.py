# https://www.acmicpc.net/problem/1780
# 이차원 배열을 나눌 때는 꼭 slice를 쓸 필요는 없다.
# 이차원 배열은 y 축 x 축 인덱스를 활용하는 것이 제일 깔끔하다.

import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**9)

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
paper_counts = [0, 0, 0]

def is_filled_with_same_num(start_x, start_y, length):
  num = paper[start_y][start_x]
  for i in range(length):
    for j in range(length):
      if paper[start_y + i][start_x + j] != num:
        return False

  return True

def divide(start_x, start_y, length):
  if is_filled_with_same_num(start_x, start_y, length):
    num = paper[start_y][start_x]
    paper_counts[num + 1] += 1
    return  
  
  for i in range(3):
    for j in range(3):
      divide(start_x + (i * length // 3), start_y + (j * length // 3), length // 3)

  return

divide(0, 0, n)

for i in paper_counts:
  print(i)
