import sys

input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()
str3 = input().strip()

common_sequences = set()

for i in range(len(str1)):
    substr = ''
    offset = 0

    for j in range(len(str2)):
        if str1[i + offset] != str2[j]:
            if substr:
                common_sequences.add(substr)
                substr = ''
            offset = 0
        
        if str1[i + offset] == str2[j]:
            substr += str2[j]
            offset += 1

    if substr:
        common_sequences.add(substr)

for sequence in sorted(common_sequences, key=len, reverse=True):
    print(sequence)