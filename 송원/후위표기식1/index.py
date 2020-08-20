import sys
sys.stdin = open("input.txt", "rt")

notation = input()
priority = {
  '(': 0,
  '+': 1,
  '-': 1,
  '*': 2,
  '/': 2
}

answer = ''
stack = []

for i in notation:
  if i.isalpha():
    answer += i
  else:
    if len(stack) == 0:
      stack.append(i)
    else:
      if i == ')':
        while stack[-1] != '(':
          answer += stack.pop()
        stack.pop()

      elif i == '(':
        stack.append(i)
      else:
        while priority[stack[-1]] >= priority[i]:
          answer += stack.pop()
          if len(stack) == 0:
            break
        stack.append(i)
      
while len(stack) != 0:
  answer += stack.pop()

print(answer)