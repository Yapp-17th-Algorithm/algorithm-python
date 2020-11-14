import sys
sys.setrecursionlimit(2000000)
sys.stdin = open("input.txt", "r")

n = int(input())
numbers = list(map(int, input().split()))
length = len(numbers)
candidates = set()

def DFS(index, total):
  global candidates
  if index >= length:
    return
  
  candidates.add(total + numbers[index])
  
  DFS(index + 1, total + numbers[index])
  DFS(index + 1, total)
  
DFS(0, 0)

i = 1
while True:
  if i not in candidates:
    print(i)
    break
  i += 1