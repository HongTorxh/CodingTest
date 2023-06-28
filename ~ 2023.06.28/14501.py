import sys
input = sys.stdin.readline

n = int(input())
t = []
p = []
sum = 0
result = 0
for i in range(0,n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(0,n):
    sum = t[i]
    while(sum > n):
        

        