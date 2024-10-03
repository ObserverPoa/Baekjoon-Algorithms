'''
Trie에 단어를 한개씩 추가하면서 
최대 공통 접두사 길이, 문자열 S의 최소 인덱스, 문자열 T의 최소 인덱스를 갱신해나간다.
words 인덱스 순서대로 Trie에 단어가 추가되기 때문에, 
자연스럽게 각 문자가 속한 최소 인덱스 문자열의 인덱스가 같이 저장된다.
'''
import sys

input = sys.stdin.readline

N = int(input())

words = [input().strip() for _ in range(N)]

trie = {} # Key: 문자, Value: (문자가 속한 문자열의 인덱스, 자식 문자 딕셔너리)
max_len = 0 # 최대 공통 접두사 길이
min_s_idx = N # 문자열 S의 최소 인덱스
min_t_idx = N # 문자열 T의 최소 인덱스

for i, word in enumerate(words):
    node = trie # 딕셔너리
    last_common = None # 공통 접두사의 마지막 문자 (문자열 S 인덱스, 깊이)

    # Trie를 탐색하여 last_common을 찾고, 현재 단어를 Trie에 추가
    for depth, char in enumerate(word, 1):
        if char in node:
            last_common = (node[char][0], depth)
            node = node[char][1]
        else:
            next_node = {}
            node[char] = (i, next_node)
            node = next_node

    if last_common is not None:
        s_idx, depth = last_common

        # 더 좋은 조건의 공통 접두사인 경우, 최대 길이와 최소 인덱스들을 갱신한다.
        if depth > max_len \
            or (depth == max_len and s_idx < min_s_idx) \
            or (depth == max_len and s_idx == min_s_idx and i < min_t_idx):
            max_len = depth
            min_s_idx = s_idx
            min_t_idx = i

print(words[min_s_idx])
print(words[min_t_idx])