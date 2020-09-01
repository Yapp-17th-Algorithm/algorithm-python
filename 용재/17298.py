# https://www.acmicpc.net/problem/17298
# 오큰수

N = int(input())

inputNumbers = list(map(int, input().split()))

answer = [-1 for _ in range(N)]

stack = []

stack.append(0)

index = 1

while stack and index < N:
  while stack and inputNumbers[stack[-1]] < inputNumbers[index]:
    answer[stack[-1]] = inputNumbers[index]
    stack.pop()
  stack.append(index)
  index += 1

print(' '.join(map(str, answer)))