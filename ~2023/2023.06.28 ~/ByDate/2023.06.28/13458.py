import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0
for i in A:
    if(i < B):
        continue
    temp = (i -B) % C
    if(temp == 0):
        result+= (i- B) // C
    else:
        result+= (i-B) // C + 1

print(result+n)