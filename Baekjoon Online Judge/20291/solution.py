'''
파일명을 입력받으면서 확장자를 카운팅하고,
(확장자, 개수)들을 확장자 사전순으로 정렬해서 출력한다.
'''
import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

counter = defaultdict(int)
for _ in range(N):
    extension = input().strip().split('.')[1]
    counter[extension] += 1

# 확장자 사전순으로 정렬해서 카운팅 출력
for extension, count in sorted(counter.items()):
    print(f'{extension} {count}')
