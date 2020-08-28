# https://www.acmicpc.net/problem/1918
# 후위 표기식

getText = input()

symbolPriority = {
  '(': 0,
  '+': 1,
  '-': 1,
  '*': 2,
  '/': 2,
}

result = []
stack = []

for each in getText:
  if 'A' <= each <= 'Z':
    result.append(each)
  elif each == '(':
    stack.append(each)
  elif each == ')':
    while stack and stack[-1] != '(':
      result.append(stack.pop())
    stack.pop()
  else:
    while stack and symbolPriority[each] <= symbolPriority[stack[-1]]:
      result.append(stack.pop())
    stack.append(each)

stack.reverse()

answer = ''.join(result + stack)

print(answer)

