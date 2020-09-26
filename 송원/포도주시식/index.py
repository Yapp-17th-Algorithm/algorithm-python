import sys
sys.stdin = open("input.txt", "r")

n = int(input())
wines = [int(input()) for _ in range(n)]

global maxTotal
maxTotal = 0

def checkCount():
  if len(wines) >= 3:
    for i in range(len(wines)):
      if i < len(wines) - 2:
        if wines[i] == -1 and wines[i + 1] == -1 and wines[i + 2] == -1:
          return True
  return False  

def DFS(index, total):
  global maxTotal
  if index >= len(wines):
    if maxTotal < total:
      maxTotal = total
    return
  
  temp = wines[index]
  wines[index] = -1
  
  if checkCount():
    wines[index] = temp
    DFS(index + 1, total)
  else:
    DFS(index + 1, total + temp)
    DFS(index + 1, total)
    
DFS(0, 0)
print(maxTotal)



