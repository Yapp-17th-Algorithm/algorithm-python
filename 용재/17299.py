# https://www.acmicpc.net/problem/17299
# 오등큰수

N = int(input())

inputNumbers = list(map(int, input().split()))

answer = [-1 for _ in range(N)]

# setInput = set(inputNumbers)

# F = {}

# for i in setInput:
#   F[i] = inputNumbers.count(i)

# print(F)

F = [0 for _ in range(10000000)]

for i in inputNumbers:
  F[i] += 1

stack = []

stack.append(0)

index = 1

while stack and index < N:
  while stack and F[inputNumbers[stack[-1]]] < F[inputNumbers[index]]:
    answer[stack[-1]] = inputNumbers[index]
    stack.pop()
  stack.append(index)
  index += 1

print(' '.join(map(str, answer)))