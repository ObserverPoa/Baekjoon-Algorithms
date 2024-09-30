'''
중복 없는 단어들을 길이가 짧은 순, 사전 순으로 정렬한다.
'''
import sys

input = sys.stdin.readline

N = int(input())

words = set([ input().strip() for _ in range(N) ])

for word in sorted(words, key=lambda x: (len(x), x)):
    print(word)