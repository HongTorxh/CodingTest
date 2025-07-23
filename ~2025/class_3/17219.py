import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())

dic = defaultdict(str)

for _ in range(n):
    site, password = map(str, input().rstrip().split())
    dic[site] += password

for _ in range(m):
    print(dic[input().rstrip()])
