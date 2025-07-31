# 2025.07.31 2
# 트리 순회
import sys
from collections import defaultdict, deque
input = sys.stdin.readline
n = int(input())
parent = [[-1] * 2 for _ in range(n+1)]
def alpha_to_int(alpha):
    return ord(alpha) - 64
def num_to_alpha(num):
    return chr(num + 64)
for i in range(1,n+1):
    root, left, right = input().split()
    root_idx = alpha_to_int(root)
    if left != '.':
        parent[root_idx][0] = alpha_to_int(left)  
    if right != '.':
        parent[root_idx][1] = alpha_to_int(right)
# 전위 순회
def preorder(node):
    if node == -1:
        return
    print(num_to_alpha(node), end='')  # 개행 제거
    left, right = parent[node]
    # print(left, right)
    preorder(left)
    preorder(right)
# 중위 순회
def inorder(node):
    left, right = parent[node]
    if node == -1:
        return
    inorder(left)         
    print(num_to_alpha(node), end='')  
    inorder(right)
#후위 순회
def postorder(node):
    left, right = parent[node]
    if node == -1:
        return
    postorder(left)
    postorder(right)
    print(num_to_alpha(node), end="")
preorder(1)
print()
inorder(1)
print()
postorder(1)