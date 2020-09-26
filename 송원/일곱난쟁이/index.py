import sys
sys.stdin = open("input.txt")

dwarfs = [int(input()) for _ in range(9)]

for i in range(len(dwarfs) - 1):
  for j in range(i + 1, len(dwarfs)):
    pickedDwarfs = dwarfs.copy()
    del pickedDwarfs[i]
    del pickedDwarfs[j - 1]
    if sum(pickedDwarfs) == 100:
      pickedDwarfs.sort()
      for k in pickedDwarfs:
        print(k)
      sys.exit(0)

# 마지막에 틀리네 음 예외 케이스 하나를 더 생각해봐야 하나 본데