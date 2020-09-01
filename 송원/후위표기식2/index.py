import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
expression = input()
operandValues = [int(input()) for i in range(n)]
operands = []
valueDict = {}

for i in expression:
  if i.isalpha() and i not in operands:
    operands.append(i)

for i in range(len(operands)):
  valueDict[operands[i]] = operandValues[i]

stack = []

for i in expression:
  if i.isalpha():
    stack.append(str(valueDict[i]))
  else:
    back = stack.pop()
    front = stack.pop()
    
    stack.append(str(eval(front + i + back)))

print('%.2f' % float(stack[0]))

# 뭔 차이지...?