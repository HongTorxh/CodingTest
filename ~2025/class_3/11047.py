import sys
input = sys.stdin.readline

# 동전을 적절히 사용하여 k로 만들기
# 오름차순으로 주어지기 때문에
# reverse하고 필요 갯수만큼 넣으면 될듯?
n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.reverse()

s = 0 # 현재까지의 합산
result = 0 # 결과

for i in arr:
    if i > k or s + i > k:
        continue
    if s == k:
        break
    temp = (k-s) // i
    s += i * temp
    result += temp

print(result)