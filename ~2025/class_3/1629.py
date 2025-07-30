# 2025.07.30 3
# 곱셈
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def d(a, b, c):
    if b == 0:
        return 1
    half = d(a, b // 2, c)
    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c

print(d(a, b, c))
