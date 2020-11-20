# https://www.acmicpc.net/problem/9663
# 1차원 리스트를 사용하여, 인덱스 번호를 체스판의 행 번호 / 각 인덱스의 value를 열 번호로 생각
from sys import stdin

N = int(stdin.readline())
ans = 0
board = [-1] * N

def promising(cdx):
    for j in range(cdx):
        if board[cdx] == board[j] or cdx - j == abs(board[cdx] - board[j]):
            return False
    return True

def put_queen(cnt):
    global ans
    if cnt == N:
        ans += 1
        return
    for i in range(N):
        board[cnt] = i
        if promising(cnt):
            put_queen(cnt+1)

put_queen(0)
print(ans)

