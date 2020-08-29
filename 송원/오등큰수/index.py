import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
sequence = list(map(int, input().split()))
sequenceSet = set(sequence)
answer = []
F = {}

maxCount = 0

for i in sequenceSet:
  count = sequence.count(i)
  if count > maxCount:
    maxCount = count
  F[i] = count

def NGF(index):
  if F[sequence[index]] == maxCount:
    return answer.append(-1)

  for i in range(index + 1, len(sequence)):
    if F[sequence[index]] < F[sequence[i]]:
      return answer.append(sequence[i])
  return answer.append(-1)

for index in range(len(sequence)):
  NGF(index)

print(' '.join([str(i) for i in answer]))

# 일단 F 값이 제일 큰 수는 무조건 -1임