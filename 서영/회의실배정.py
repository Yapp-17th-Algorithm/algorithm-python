# https://www.acmicpc.net/problem/1931

N = int(input())
time = []
for _ in range(N):
    a, b = map(int, input().split())
    time.append((a, b))
time.sort(key=lambda x: (x[1], x[0]))

# 회의 시작시간으로 정렬한 뒤, 2중 for문 쓰니까 시간초과..
# ans = 0
# for i in range(N):
#     cnt = 1
#     st = time[i]
#     for j in range(i, N):
#         if time[j][0] >= st[1]:
#             cnt += 1
#             st = time[j]
#     ans = max(ans, cnt)
# print(ans)

# 회의 끝나는 시간으로 정렬
ans = 1
last = time[0]
for i in range(1, N):
    if time[i][0] >= last[1]:
        ans += 1
        last = time[i]
print(ans)