# https://www.acmicpc.net/problem/1935
# 후위 표기식 2

N = int(input())
getText = input()

inputNumbers = [int(input()) for _ in range(N)]

stack = []

for each in getText:
  if 'A' <= each <= 'Z':
    stack.append(inputNumbers[ord(each) - 65])
  else:
    right = stack.pop()
    left = stack.pop()
    if each == '+':
      stack.append(left + right)
    elif each == '-':
      stack.append(left - right)
    elif each == '*':
      stack.append(left * right)
    else:
      stack.append(left / right)

print('%.2f' % stack[0])

