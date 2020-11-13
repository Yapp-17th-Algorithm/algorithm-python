# https://www.acmicpc.net/problem/2667


def is_valid_coordinate(size, y, x):
    return 0 <= y and y < size and 0 <= x and x < size


def not_visit(visited, y, x):
    return visited[y][x] == False


def dfs(JIDO, visited, size, y, x):
    if visited[y][x]:
        return 0
    houses = 0
    if not_visit(visited, y, x) and JIDO[y][x] == 1:
        houses += 1
    visited[y][x] = True  # 방문처리 우선
    TOP, DOWN = [-1, 0], [1, 0]
    LEFT, RIGHT = [0, -1], [0, 1]
    directions = [TOP, DOWN, LEFT, RIGHT]
    for direction in directions:
        next_y = y - direction[0]
        next_x = x - direction[1]
        if is_valid_coordinate(size, next_y, next_x) and not_visit(visited, next_y, next_x) and JIDO[next_y][next_x] == 1:
            # 다음 좌표가 valid해야하고, 방문하지 않았어야 하며, 집이어야함
            if JIDO[y][x] == 1:  # 현재 위치가 집이어야만 다음 집과 같은 단지이므로 해당 조건을 넣어줌
                houses += dfs(JIDO, visited, size, next_y, next_x)
    return houses


def solution():
    N = int(input())  # 지도의 크기
    JIDO = []  # map은 예약어이기 때문에 map으로 짓지 못함. -> jido
    visited = [[False] * N for _ in range(N)]  # False = 방문 X, True = 방문 O

    for i in range(N):
        JIDO.append([])
        line = input()
        for j in line:
            JIDO[i].append(int(j))

    danji = []
    for y, JIDO_y in enumerate(JIDO):
        for x in range(len(JIDO_y)):
            house_cnt = dfs(JIDO, visited, N, y, x)
            if house_cnt > 0:
                danji.append(house_cnt)

    danji.sort()
    print(len(danji))
    for i in danji:
        print(i)


solution()
