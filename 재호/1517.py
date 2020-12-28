# https://www.acmicpc.net/problem/1517

from sys import setrecursionlimit

setrecursionlimit(10 ** 6)


def merge(low, mid, high, A, B, result):
    i, j, k = low, mid + 1, low
    while i <= mid and j <= high:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
            result[0] += mid - i + 1
        k += 1

    if (i > mid):
        for idx in range(j, high + 1):
            B[k] = A[idx]
            k += 1
    else:
        for idx in range(i, mid + 1):
            B[k] = A[idx]
            k += 1

    for idx in range(low, high + 1):
        A[idx] = B[idx]


def mergeSort(low, high, A, B, result):
    if (low < high):
        mid = (low + high) // 2
        mergeSort(low, mid, A, B, result)
        mergeSort(mid + 1, high, A, B, result)
        merge(low, mid, high, A, B, result)


def solution():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    result = [0]
    mergeSort(0, N - 1, A, B, result)
    print(result[0])


solution()
