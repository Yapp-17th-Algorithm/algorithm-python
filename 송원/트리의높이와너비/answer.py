import sys
sys.stdin = open("input.txt", "r")
n = int(input())  
parentNode = [-1]*(n+1)
tree = {}
root = 0

for _ in range(n):  # 1) 트리 형태 만들기
    v, left, right = map(int, input().split(' '))
    tree[v] = [left, right]
    if left != -1:
        parentNode[left] = v
    if right != -1:
        parentNode[right] = v

for i in range(1, n+1):  # 2) 루트 노드 찾기
    if parentNode[i] == -1:
        root = i

level_min = [n]*(n+1)  # 각 레벨의 최소, 최대 idx 저장
level_max = [0]*(n+1)
level = [0]*(n+1)
level[root] = 1
cur = 0


def in_order(key): # 3) 중위 순회
    global cur
    if tree[key][0] != -1:
        level[tree[key][0]] = level[key] + 1
        in_order(tree[key][0])

    cur += 1
    
    if level_min[level[key]] > cur:
        level_min[level[key]] = cur
    if level_max[level[key]] < cur:
        level_max[level[key]] = cur

    if tree[key][1] != -1:
        level[tree[key][1]] = level[key] + 1
        in_order(tree[key][1])

    return


in_order(root)

result = 0
result_idx = 0

for i in range(1, n+1): # 4) 차이 찾기
    diff = level_max[i]-level_min[i]+1
    if result < diff:
        result = diff
        result_idx = i

print(result_idx, result)