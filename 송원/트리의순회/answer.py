import sys
sys.setrecursionlimit(10**9)
 
n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))#중위순회
postorder = list(map(int, sys.stdin.readline().split()))#후위순회
in_location=[0 for _ in range(n+1)]#인자를 찾을때 한번에 찾기위해서
for i in range(n):
  in_location[inorder[i]]=i
 
def pre_order(in_l,in_r,post_l,post_r): #중위순회 범위 후위순회 범위
  if post_l <= post_r:
    parents=postorder[post_r]#후위순회에서 부모노드 찾기

    print(parents,end=" ")
    p_index=in_location[parents]
    l_count=p_index-in_l#왼쪽인자 갯수
    r_count=in_r-p_index#오른쪽인자 갯수

    pre_order(in_l , in_l+l_count-1 , post_l , post_l+l_count-1)#부모노드를 기준으로 왼쪽노드
    pre_order(in_r-r_count+1 , in_r , post_r-r_count , post_r-1)#부모노드 기준 오른쪽
 
pre_order(0,n-1,0,n-1)
