import sys
sys.stdin = open("input.txt", "r")

n = int(input())

tree_dict = {}

for i in range(n):
  root, left, right = input().split()
  tree_dict[root] = [left, right]


def pre_order(node):
  if node != '.':
    print(node, end="")
    pre_order(tree_dict[node][0])
    pre_order(tree_dict[node][1])
  

def in_order(node):
  if node != '.':
    in_order(tree_dict[node][0])
    print(node, end="")
    in_order(tree_dict[node][1])
  

def post_order(node):
  if node != '.':
    post_order(tree_dict[node][0])
    post_order(tree_dict[node][1])
    print(node, end="")

pre_order('A')
print()
in_order('A')
print()
post_order('A')