import sys
input = sys.stdin.readline

n = int(input())
result = 0
a = 1
for i in range(n):
    a += 6 * i
    if n <= a:
        result = i + 1
        break
print(result)