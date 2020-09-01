# https://www.acmicpc.net/problem/17413
# 단어 뒤집기

getText = input()

result = []
stack = []

flag = False

for each in getText:
  if each == '>':
    result.append(each)
    flag = False
  elif each == '<' or flag:
    while stack:
      result.append(stack.pop())
    result.append(each)
    flag = True

  elif each == ' ':
    while stack:
      result.append(stack.pop())
    result.append(each)
  else:
    stack.append(each)

stack.reverse()

print(''.join(result + stack))