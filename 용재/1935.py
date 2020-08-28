N = int(input())
getText = input()

inputNumbers = []

for i in range(N):
  inputNumbers.append(int(input()))

stack = []

for each in getText:
  if 'A' <= each <= 'Z':
    stack.append(inputNumbers[ord(each) - 65])
  else:
    right = stack.pop()
    left = stack.pop()
    if each == '+':
      stack.append(left + right)
    if each == '-':
      stack.append(left - right)
    if each == '*':
      stack.append(left * right)
    if each == '/':
      stack.append(left / right)

print('%.2f' % stack[0])

