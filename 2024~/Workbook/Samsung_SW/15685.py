import sys
input = sys.stdin.readline

# 100 * 100판
board = [[0] * 100 for _ in range(100)]
# 0, 1, 2, 3
direction = [(0, 1), (-1, 0), (0, -1), (0, 1)]
curves = []
n = int(input())
for _ in range(n):
    x, y, d, g = map(int, input().split())
    curves.append((x, y, d, g))

for curve in curves:
    x, y, d, g = curve
    while g <= 0:
