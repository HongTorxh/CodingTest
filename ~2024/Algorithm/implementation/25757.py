import sys
input = sys.stdin.readline

n, t = map(str, input().split())
n = int(n)

s = set()

for _ in range(n):
    name = input().rstrip()
    s.add(name)

if t == "Y":
    print(len(s))
elif t == "F":
    print(len(s) // 2)
else:
    print(len(s) // 3)