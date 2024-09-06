'''
모든 부분 문자열을 set에 중복없이 저장해서 개수를 구한다. 
'''
import sys

input = sys.stdin.readline

S = input().strip()

parts = set()

for left in range(len(S)):
    for right in range(left, len(S)):
        parts.add(S[left:right + 1])

print(len(parts))