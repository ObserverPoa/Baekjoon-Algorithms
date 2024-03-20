# https://www.acmicpc.net/problem/1062

import sys
import collections
import itertools

def solution(words, k):
    char_counter = collections.defaultdict(int)
    words_chars = []

    for word in words:
        chars = set()
        for char in word:
            chars.add(char)
        for char in chars:
            char_counter[char] += 1
        words_chars.append(chars)

    common_chars = [
        char 
        for [ char, count ] in char_counter.items()
        if count == len(words)
    ]

    k -= len(common_chars)

    if k < 0:
        return 0
    
    for common_char in common_chars: 
        del char_counter[common_char]
    
    general_chars = list(char_counter.keys())

    if k >= len(general_chars):
        return len(words_chars)
    
    answer = 0

    for selected_chars in itertools.combinations(general_chars, k):
        learned_chars = set([*common_chars, *selected_chars])

        answer = max(
            answer,
            len(list(filter(lambda word_chars: learned_chars >= word_chars, words_chars)))
        )   
    
    return answer
    
N, K = map(int, sys.stdin.readline().split())

words = [
    sys.stdin.readline().strip() for _ in range(N)
]

print(solution(words, K))