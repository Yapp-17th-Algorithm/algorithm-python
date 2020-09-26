import sys
sys.stdin = open("input.txt", "r")

n = int(input())
packs = list(map(int, input().split()))
packs = [(i + 1, v) for i, v in enumerate(packs)]
minCardCost = 0
selectedPackNumber = None
sortedPacks = sorted(packs, key=lambda x: x[1] / x[0])

def DFS(packNumber, cardCount, totalAmount):
  if packNumber > len(packs):
    return

  while cardCount - packs[packNumber - 1][0] > 0:
    cardCount -= packs[packNumber - 1][0]
    totalAmount += packs[packNumber - 1][1]
    # total 관리 아직 안되고 있음
  
  if cardCount == 0:
    print(totalAmount)
    sys.exit(0)
    
  else:
    # BFS 가 맞는건가
    for j in range(packNumber + 1, len(packs)):
      DFS(j, cardCount, totalAmount)

for i in range(len(sortedPacks)):
  DFS(i, n, 0)






# while n != 0:
#   for i in range(1, len(packs)):
#     if packs[i] / i > minCardCost and packs[i] != 0:
#       minCardCost = packs[i] / i
#       selectedPackNumber = i
#   while n - selectedPackNumber > 0:
#     n -= selectedPackNumber
#     total += packs[selectedPackNumber]
#   packs[selectedPackNumber] = 0



# if n == 0:
#   print(total)
# else:
#   while n != 0:


# 구매한 카드팩에 포함되어 있는 카드 개수의 합은 N과 같아야 한다.
# N개보다 많은 개수의 카드를 산 다음, 나머지 카드를 버려서 N개를 만드는 것은 불가능하다.




