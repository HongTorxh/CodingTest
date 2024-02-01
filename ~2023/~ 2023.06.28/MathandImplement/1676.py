import sys
input = sys.stdin.readline

n = int(input())

result = 1

for i in range(1,n+1):
    result = result * i 

count = 0
while result >= 0 :
    temp = result % 10
    if temp == 0:
        count += 1
        result = result // 10
    else:
        break
print(count)