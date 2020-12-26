import sys
sys.stdin = open("input.txt", "r")

n = int(input())
n_list = list(map(int, input().split()))
sorted_list = sorted(n_list)
swap_count = 0

i = 0
while i <= n - 1:
  if n_list[i] != sorted_list[i]:
    index = sorted_list.index(n_list[i])
    swap_count += index - i
    temp = n_list[i]
    del n_list[i]
    n_list.insert(index, temp)
  else:
    i += 1

print(swap_count)