# https://www.acmicpc.net/problem/12015


def solution():
    N = int(input())
    A = list(map(int, input().split()))
    dp = [0]
    for i in range(N):
        low, high = 0, len(dp) - 1

        while low <= high:
            mid = (low + high) // 2
            if dp[mid] < A[i]:
                low = mid + 1
            else:
                high = mid - 1

        if low > len(dp) - 1:
            dp.append(A[i])
        else:
            dp[low] = A[i]

    print(len(dp) - 1)


solution()
