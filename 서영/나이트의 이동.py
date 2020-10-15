# https://www.acmicpc.net/problem/7562

from collections import deque

T = int(input())


def bfs(tx, ty):
    q = deque([(tx, ty, 0)])
    while q:
        x, y, cnt = q.popleft()
        if (x, y) == goal:
            return cnt
        for dx, dy in (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1):
            if 0 <= x+dx < I and 0 <= y+dy < I:
                if not visit[x+dx][y+dy]:
                    q.append((x+dx, y+dy, cnt+1))
                    visit[x+dx][y+dy] = True


for _ in range(T):
    I = int(input())
    cur = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))
    visit = [[False] * I for _ in range(I)]
    ans = bfs(cur[0], cur[1])
    print(ans)