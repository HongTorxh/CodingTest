import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dic = defaultdict(list)
    for _ in range(n):
        a, b = map(str, input().rstrip().split())
        dic[b].append(a)
    result = 1
    for value in dic.values():
        result *= (len(value) + 1)
    print(result - 1)