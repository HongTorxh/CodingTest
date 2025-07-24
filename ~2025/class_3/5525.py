# 2025.07.24 3
# IOIOI

n = int(input())
m = int(input())
s = input().rstrip()

result = 0
cnt = 0
i = 0
while i < m - 2:
    if s[i:i+3] == "IOI":
        cnt += 1
        if cnt == n:
            result += 1
            cnt -= 1
        i += 2
    else:
        cnt = 0
        i += 1
print(result)