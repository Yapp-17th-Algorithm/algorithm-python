# https://www.acmicpc.net/problem/1406
# 에디터

getText = list(input())

N = int(input())

inputNumbers = [input().split() for _ in range(N)]

L = len(getText)

restText = []

COMMAND, CHAR = 0, 1
for i in inputNumbers:
  if i[COMMAND] == "L" and getText:
    restText.append(getText.pop())
  elif i[COMMAND] == "D" and restText:
    getText.append(restText.pop())
  elif i[COMMAND] == "B" and getText:
    getText.pop()
  elif i[COMMAND] == "P":
    getText.append(i[CHAR])

print(''.join(getText + restText[::-1]))