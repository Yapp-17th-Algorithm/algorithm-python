# https://www.acmicpc.net/problem/1744


def solution():
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    nums.sort()
    answer = 0
    l, r = 0, len(nums) - 1
    while l < r and nums[l] < 1 and nums[l + 1] < 1:
        answer += nums[l] * nums[l + 1]
        l += 2
    while r > 0 and nums[r] > 1 and nums[r - 1] > 1:
        answer += nums[r] * nums[r - 1]
        r -= 2
    while r >= l:
        answer += nums[r]
        r -= 1
    print(answer)


solution()
