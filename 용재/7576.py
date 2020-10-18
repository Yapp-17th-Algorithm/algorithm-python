from collections import deque
from typing import List

# https://www.acmicpc.net/problem/7576
# 토마토

def bfs(M: int, N: int, box: List[int]) -> int:
    result = -1

    while queue:
      result+= 1
      for _ in range(len(queue)):
        x, y = queue.popleft()

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]

            if 0 <= cx < N and 0 <= cy < M and box[cx][cy] == 0:
                box[cx][cy] = box[x][y] + 1
                queue.append([cx, cy])

    for i in box:
      if 0 in i:
        return -1

    return result

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

M, N = [int(i) for i in input().split()]

box = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append([i, j])

print(bfs(M, N, box))
