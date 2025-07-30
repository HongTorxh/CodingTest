# 2025.07.30 1
# N과 M (12)
import sys, itertools
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(set(map(int, input().split())))

combination = itertools.combinations_with_replacement(arr, m)

for combi in combination:
    print(*combi)