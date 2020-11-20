#보드 가장자리에 0을 추가해서 좌표의 보드값이 0일 때 떨어진것으로 간주
from collections import deque

dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
def sol():
    while q:
        x1, y1, x2, y2 = q.popleft()
        if ck[x1][y1][x2][y2] > 10: break
        for i in range(4):
            xx1, yy1 = x1+dx[i], y1+dy[i]
            xx2, yy2 = x2+dx[i], y2+dy[i]
            if Map[xx1][yy1]==0 and Map[xx2][yy2]==0:
                continue
            if Map[xx1][yy1]==0: return ck[x1][y1][x2][y2]
            if Map[xx2][yy2]==0: return ck[x1][y1][x2][y2]
            if Map[xx1][yy1] == '#':
                xx1, yy1 = x1, y1
            if Map[xx2][yy2] == '#':
                xx2, yy2 = x2, y2
            if not ck[xx1][yy1][xx2][yy2]:
                ck[xx1][yy1][xx2][yy2] = ck[x1][y1][x2][y2]+1
                q.append([xx1, yy1, xx2, yy2])
    return -1

N, M = map(int, input().split(' '))
Map = [[0]*(M+2)]
for _ in range(N):
    Map.append([0]+list(input())+[0])
Map.append([0]*(M+2))
coin = []
for i in range(N+2):
    for j in range(M+2):
        if Map[i][j] == 'o':
            coin.append(i)
            coin.append(j)
            Map[i][j] = '.'
ck = [[[[0]*(M+2) for _ in range(N+2)] for _ in range(M+2)] for _ in range(N+2)]
ck[coin[0]][coin[1]][coin[2]][coin[3]] = 1
q = deque()
q.append([coin[0], coin[1], coin[2], coin[3]])
print(sol())

# 와...동전 두개의 x,y 좌표들을 4차원 배열 안에 담을 생각을 하다니...