import sys
from collections import deque
sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())

back_track = [0] * 100001
visited = [0] * 100001
visited[n] = 1
Q = deque()
Q.append(n)

while Q:
  pos = Q.popleft()
  
  if pos == k:
    count = 0
    answer = []
    while pos != n:
      count += 1
      answer.append(str(pos))
      pos = back_track[pos]

    answer.append(str(n))
    answer.reverse()
    print(count)
    print(' '.join(answer))
    sys.exit(0)

  for new_pos in (pos + 1, pos * 2, pos - 1):
    if 0 <= new_pos < 100001 and visited[new_pos] != 1:
      visited[new_pos] = 1
      back_track[new_pos] = pos
      Q.append(new_pos)


