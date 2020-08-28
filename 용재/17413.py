getText = input()

result = []
stack = []

flag = False

for each in getText:
  if each == '>':
    result.append(each)
    flag = False
  elif each == '<' or flag == True:
    while stack:
      result.append(stack.pop())
    result.append(each)
    flag = True

  elif each == ' ':
    while stack:
      result.append(stack.pop())
    result.append(' ')
  else:
    stack.append(each)

stack.reverse()

print(''.join(result + stack))