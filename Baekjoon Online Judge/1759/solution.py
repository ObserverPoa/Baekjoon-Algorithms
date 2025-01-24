import sys
from itertools import combinations

input = sys.stdin.readline

L, C = map(int, input().split())

chars = input().split()

def is_valid_passowrd(text):
    vowel_count, consonant_count = 0, 0
    for char in text:
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowel_count += 1
        else:
            consonant_count += 1
    return vowel_count >= 1 and consonant_count >= 2

passwords = []

for combination in combinations(chars, L):
    if is_valid_passowrd(combination):
        passwords.append(''.join(sorted(combination)))

for password in sorted(passwords):
    print(password)

