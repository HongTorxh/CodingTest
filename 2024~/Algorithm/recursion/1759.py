import sys
import itertools

input = sys.stdin.readline


l, c = map(int, input().split())
arr = list(map(str, input().rstrip().split()))

vowels = {'a', 'e', 'i', 'o', 'u'}
arr.sort()


for combo in itertools.combinations(arr, l):

    vowel_count = sum(1 for char in combo if char in vowels)
    consonant_count = l - vowel_count
    
    
    if vowel_count >= 1 and consonant_count >= 2:
        print(''.join(combo))
