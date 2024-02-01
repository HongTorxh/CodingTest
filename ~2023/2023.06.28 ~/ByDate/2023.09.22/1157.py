import sys
input = sys.stdin.readline

n = input()

n = n.lower()
alphabet = [0] * 26

for i in range(0,len(n)-1):
    alphabet[ord(n[i])-97] += 1

max = -1
max_index = 0
count = 0
for i in range(len(alphabet)):
    if max == alphabet[i]:
        count += 1
    if max < alphabet[i]:
        max = alphabet[i]
        max_index = i
        count = 1

if count > 1:
    print("?")
else:
    print(chr(max_index+65))