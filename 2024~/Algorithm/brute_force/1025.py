import sys, math
input = sys.stdin.readline

# 9 * 9가 최대 사이즈
# 공차가 3 이상이 불가 # 때문에 공차가 2까지로 제한

def is_square(string):
     num = int(string)
     root = int(math.isqrt(num))
     return root * root == num


n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(input().rstrip()))
result = -1
for i in range(n):
    for j in range(m):
        for dx in range(-n, n):
            for dy in range(-m, m):
                if dx == 0 and dy == 0:
                    continue
                temp = ''
                x, y = i, j
                while 0 <= x < n and 0 <= y < m:
                    temp += arr[x][y]
                    
                    if is_square(temp):
                        result = max(result, int(temp))
                    x += dx
                    y += dy

print(result)
