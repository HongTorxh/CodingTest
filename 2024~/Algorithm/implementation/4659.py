import sys
input = sys.stdin.readline

vowels = {'a','e','i','o','u'}
def checkContinuous(word):
    vowel_cnt = 0
    consonant_cnt = 0
    for w in word:
        if w in vowels:
            vowel_cnt += 1
            consonant_cnt = 0
        else:
            vowel_cnt = 0
            consonant_cnt += 1
        if vowel_cnt == 3 or consonant_cnt == 3:
            return False
    for i in range(len(word) - 1):
        if word[i] == word[i+1] and word[i : i+2] not in ("ee", "oo"):
            return False
    return True
while True:
    tmp = input().rstrip()
    if tmp == "end":
        break
    if not any(v in tmp for v in vowels):
        print(f"<{tmp}> is not acceptable.")
        continue
    if not checkContinuous(tmp):
        print(f"<{tmp}> is not acceptable.")
        continue
    print(f"<{tmp}> is acceptable.")