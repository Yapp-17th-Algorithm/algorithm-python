# https://www.acmicpc.net/problem/2263

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


def go(post_order_list, in_order_start, in_order_end, post_order_start,
        post_order_end, order_of_in_order):
    if in_order_start > in_order_end or post_order_start > post_order_end:
        return
    print(post_order_list[post_order_end], end=" ")
    root_idx = order_of_in_order[post_order_list[post_order_end]]
    l = root_idx - in_order_start
    go(post_order_list, in_order_start, root_idx -
       1, post_order_start, post_order_start + l - 1, order_of_in_order)
    go(post_order_list, root_idx + 1, in_order_end, post_order_start +
       l, post_order_end - 1, order_of_in_order)


def solution():
    n = int(stdin.readline())
    order_of_in_order = {}
    in_order_list = list(map(int, stdin.readline().split()))
    for i in range(len(in_order_list)):
        order_of_in_order[in_order_list[i]] = i
    post_order_list = list(map(int, stdin.readline().split()))
    go(post_order_list, 0, n - 1, 0, n - 1, order_of_in_order)


solution()
