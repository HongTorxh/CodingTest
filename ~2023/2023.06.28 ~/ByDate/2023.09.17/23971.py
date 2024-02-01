import sys
input = sys.stdin.readline

h, w, n, m = map(int, input().split())

h = (h // (n+1) + 1) if h % (n+1) != 0 else h // (n+1)
w = (w // (m+1) + 1) if w % (m+1) != 0 else w // (m+1)


print(h * w)