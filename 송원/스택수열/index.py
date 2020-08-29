import sys
sys.stdin = open("input.txt", "r")

n = int(input())
inputList = []
stack = []
result = []

for i in range(n):
  inputList.append(int(input()))

num = 1
i = 0
prev = 0

while len(inputList) != 0:
  if inputList[0] < prev:
    if inputList[0] != stack[-1]:
      result = False
      break
    else:
      stack.pop()
      result.append('-')
      prev = inputList.pop(0)
    continue

  while num < inputList[0]:
    stack.append(num)
    result.append('+')
    num += 1

  # stack.append(num)
  # stack.pop() 을 생략
  result.append('+')
  result.append('-')
  inputList.pop(0)
  prev = num
  num += 1
  
if result == False:
  print('NO')
else:
  for i in result:
    print(i)

  
# 어라 NO를 안하네