import sys
from collections import defaultdict
input = sys.stdin.readline

dictionary = defaultdict(int)
reverse = defaultdict(str)
n, m = map(int, input().split())

for i in range(1,n + 1):
    temp = input().strip()
    dictionary[temp] += i
    reverse[i] += temp
for i in range(m):
    temp = input().strip()
    if temp.isdigit():
        print(reverse[int(temp)])
    else:
        print(dictionary[temp])