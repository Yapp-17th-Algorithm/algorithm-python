import sys
sys.stdin = open("input.txt", "r")

text = list(input())
cursor = len(text)
n = int(input())

for i in range(n):
  inputs = input().split()
  if inputs[0] == 'L':
    if cursor != 0:
      cursor -= 1
  elif inputs[0] == 'D':
    if cursor != len(text):
      cursor += 1
  elif inputs[0] == 'B':
    if cursor != 0:
      del text[cursor - 1]
      cursor -= 1
  elif inputs[0] == 'P':
    value = inputs[1]
    text.insert(cursor, value)
    cursor += 1

print(''.join(text))

# 자르기 이거 시간 엄청 걸리는건가 보네