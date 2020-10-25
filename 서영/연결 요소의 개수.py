# https://www.acmicpc.net/problem/11724

def dfs(x):
    check[x] = True
    for n in node[x]:
        if not check[n]:
            dfs(n)


N, M = map(int, input().split())
node = [[] for _ in range(N+1)]
check = [False] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

ans = 0
for i in range(1, N+1):
    if not check[i]:
        ans += 1
        dfs(i)
print(ans)
