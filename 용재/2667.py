# https://www.acmicpc.net/problem/2667
# 단지번호붙이기

count = 0

def dfs(x: int, y: int) -> None:
    global count
    square_map[x][y] = '0'
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if square_map[nx][ny] == '1':
            dfs(nx, ny)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())

square_map = [list(input()) for _ in range(N)]

apartment = []

for i in range(N):
    for j in range(N):
        if square_map[i][j] == '1':
            count = 0
            dfs(i, j)
            apartment.append(count)

print(len(apartment))

apartment.sort()

for i in apartment:
    print(i)
