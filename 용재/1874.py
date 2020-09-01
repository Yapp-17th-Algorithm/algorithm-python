# https://www.acmicpc.net/problem/1874
# 스택수열

N = int(input())

inputNumbers = [int(input()) for _ in range(N)]

stack = []
answer = []

index = 0

flag = False

for each in inputNumbers:
  # TODO: refactoring later
  while True:
    if not stack or stack[-1] != each:
      index += 1
      answer.append('+')
      stack.append(index)
    if stack and stack[-1] == each:
      answer.append('-')
      stack.pop()
      break
    if stack and stack[-1] > each:
      flag = True
      break

if flag == True:
  print("NO")
else:
  for i in answer:
    print(i)
