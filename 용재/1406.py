# https://www.acmicpc.net/problem/1406
# 에디터

getText = list(input())

N = int(input())

inputNumbers = [str(input()) for _ in range(N)]

L = len(getText)

restText = []

for i in inputNumbers:
  if i[0] == "L":
    if len(getText) > 0:
      restText.append(getText.pop())
  elif i[0] == "D":
    if len(restText) > 0:
      getText.append(restText.pop())
  elif i[0] == "B":
    if len(getText) > 0:
      getText.pop()
  elif i[0] == "P":
    getText.append(i[2])

print(''.join(getText + restText[::-1]))