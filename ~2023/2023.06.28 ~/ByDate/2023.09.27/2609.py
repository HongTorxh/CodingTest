import sys
input = sys.stdin.readline

def gcd(a, b):
    if (a%b) == 0:
        return b
    return gcd(b, a % b)

a, b = map(int, input().split())
g = gcd(a,b)

print(g)
print((a*b) // g)
