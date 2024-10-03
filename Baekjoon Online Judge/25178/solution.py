'''
두 문자열이 세가지 조건에 맞는지 판별한다.
'''
import sys

input = sys.stdin.readline

VOWELS = ['a', 'e', 'i', 'o', 'u']

def is_duramuri(str1, str2):
    # 두 단어의 첫 글자와 마지막 글자는 서로 동일해야 한다.
    if str1[0] != str2[0] or str1[-1] != str2[-1]: 
        return False
    
    # 한 단어를 재배열해 다른 단어를 만들 수 있어야 한다.
    for char1, char2 in zip(sorted(str1), sorted(str2)):
        if char1 != char2:
            return False

    consonants1 = [char for char in str1 if char not in VOWELS]
    consonants2 = [char for char in str2 if char not in VOWELS]

    # 각 단어에서 모음(a, e, i, o, u)을 제거한 문자열은 동일해야 한다
    for char1, char2 in zip(consonants1, consonants2):
        if char1 != char2:
            return False

    return True

N = int(input())
str1 = input().strip()
str2 = input().strip()
print('YES' if is_duramuri(str1, str2) else 'NO')