import sys
from collections import deque
sys.stdin = open("input.txt", "r")

s = int(input())
Q1 = deque()
Q2 = deque()
Q1.append((1, 0))
visited = []
count = 0

def move_item(from_Q, to_Q):
  while from_Q:
    screen, clipboard = from_Q.popleft()
    if screen == s or screen + clipboard == s or screen - 1 == s:
      print(count + 1)
      sys.exit(0)

    if 0 <= screen <= 1000 and (screen, clipboard) not in visited:
      to_Q.append((screen, screen))
      to_Q.append((screen + clipboard, clipboard))
      to_Q.append((screen - 1, clipboard))
      visited.append((screen, clipboard))

while Q1 or Q2:
  if Q1:
    move_item(Q1, Q2)
  elif Q2:
    move_item(Q2, Q1)
  count += 1
