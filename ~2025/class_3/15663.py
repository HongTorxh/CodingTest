# 2025.07.29 3
# N과 M (9)
import sys
from itertools import permutations
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
result = sorted(list(set(list(permutations(arr, m)))))

for r in result:
    print(*r)