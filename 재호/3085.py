# https://www.acmicpc.net/problem/3085

from sys import stdin
import copy


def check_max_eat_cnt(box):
    answer = []

    for i in range(len(box)):
        cnt = 1
        for j in range(1, len(box)):
            if box[i][j - 1] == box[i][j]:
                cnt += 1
            else:
                answer.append(cnt)
                cnt = 1
        answer.append(cnt)

    for i in range(len(box)):
        cnt = 1
        for j in range(1, len(box)):
            if box[j - 1][i] == box[j][i]:
                cnt += 1
            else:
                answer.append(cnt)
                cnt = 1
        answer.append(cnt)

    return max(answer)


def solution():
    N = int(stdin.readline())
    box = [[c for c in stdin.readline() if c != '\n'] for _ in range(N)]
    answer = []
    answer.append(check_max_eat_cnt(box))
    for i in range(N):
        for j in range(N):
            if i + 1 != N and box[i][j] != box[i + 1][j]:
                new_box = copy.deepcopy(box)
                new_box[i][j], new_box[i + 1][j] = new_box[i + 1][j], new_box[i][j]
                answer.append(check_max_eat_cnt(new_box))
            if j + 1 != N and box[i][j] != box[i][j + 1]:
                new_box = copy.deepcopy(box)
                new_box[i][j], new_box[i][j + 1] = new_box[i][j + 1], new_box[i][j]
                answer.append(check_max_eat_cnt(new_box))
    print(max(answer))


solution()
