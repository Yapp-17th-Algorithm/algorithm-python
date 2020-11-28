# https://www.acmicpc.net/problem/16197

import sys
sys.setrecursionlimit(10**8)

COIN, EMPTY, WALL = 'o', '.', '#'
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
answer = 12

def can_i_go(y, x, N, M):
    return 0 <= y < N and 0 <= x < M

def go(board, c1y, c1x, c2y, c2x, N, M, cnt):
    global answer
    # 10번 이상 움직이면 종료
    if cnt > 10:
        return
    # 둘 다 떨어지면 종료 == 둘 다 범위 초과시 종료
    if not can_i_go(c1y, c1x, N, M) and not can_i_go(c2y, c2x, N, M):
        return
    # 하나만 떨어졌다면 answer에 append후 종료
    if not can_i_go(c1y, c1x, N, M) or not can_i_go(c2y, c2x, N, M):
        answer = min(answer, cnt)
        return
    # 여기까지 온다는 것은 움직였는데 하나만 떨어지지도 않았고 둘 다 떨어지지도 않음
    # 그 말은 움직였는데 벽이건나 빈칸이거나 동전이 있는 위치
    for i in range(4):
        n1y = c1y + dy[i]
        n1x = c1x + dx[i]
        n2y = c2y + dy[i]
        n2x = c2x + dx[i]
        if can_i_go(n1y, n1x, N, M) and board[n1y][n1x] == WALL:
            n1y -= dy[i]
            n1x -= dx[i]
        if can_i_go(n2y, n2x, N, M) and board[n2y][n2x] == WALL:
            n2y -= dy[i]
            n2x -= dx[i]
        go(board, n1y, n1x, n2y, n2x, N, M, cnt + 1)


def solution():
    N, M = map(int, input().split())
    coin_position = []
    board = [[c for c in input()] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == COIN:
                coin_position.append((i, j))
    
    c1y = coin_position[0][0]
    c1x = coin_position[0][1]
    c2y = coin_position[1][0]
    c2x = coin_position[1][1]
    for i in range(4):
        n1y = c1y + dy[i]
        n1x = c1x + dx[i]
        n2y = c2y + dy[i]
        n2x = c2x + dx[i]
        if can_i_go(n1y, n1x, N, M) and board[n1y][n1x] == WALL:
            n1y -= dy[i]
            n1x -= dx[i]
        if can_i_go(n2y, n2x, N, M) and board[n2y][n2x] == WALL:
            n2y -= dy[i]
            n2x -= dx[i]
        go(board, n1y, n1x, n2y, n2x, N, M, 1)
    print(answer if answer != 12 else -1)


solution()
