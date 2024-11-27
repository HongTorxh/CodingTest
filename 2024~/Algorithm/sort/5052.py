import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    phone_numbers = [input().strip() for _ in range(n)]
    
    phone_numbers.sort()
    
    consistent = True
    for i in range(n - 1):
        if phone_numbers[i + 1].startswith(phone_numbers[i]):
            consistent = False
            break
        
    print("YES" if consistent else "NO")