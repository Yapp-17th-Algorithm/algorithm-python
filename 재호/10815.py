# https://www.acmicpc.net/problem/10815


def solution():
    N = int(input())
    cards1 = list(map(int, input().split()))
    M = int(input())
    cards2 = list(map(int, input().split()))
    card_dict = {}
    for c in cards1:
        card_dict[c] = True
    for c in cards2:
        if c in card_dict:
            print(1, end=" ")
        else:
            print(0, end=" ")


solution()
