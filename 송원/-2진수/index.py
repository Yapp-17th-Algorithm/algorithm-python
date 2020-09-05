import sys
sys.stdin = open("input.txt", "r")

n = int(input())
result = 0

def getLength(num):
  binaryLength = 3
  temp = 1
  while abs(num) > temp * 2:
    temp *= 2
    binaryLength += 1
  return binaryLength

binaryLimit = getLength(n)

def getNumber(binary):
  result = 0
  for i in range(len(binary) -1, -1, -1):
    if binary[i] == '1':
      position = len(binary) - int(i) - 1
      number = 1
      for _ in range(position):
        number *= -2
      result += number
  return result

def DFS(binary):
  number = getNumber(binary)
  if number == n:
    print(binary)
    sys.exit(0)
  else:
    if len(binary) < binaryLimit:
      DFS(binary + '1')
      DFS(binary + '0')

if abs(n) % 2 == 0:
  DFS('0')
else:
  DFS('1')

