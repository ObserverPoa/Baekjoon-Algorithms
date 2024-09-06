'''
문자열의 문자를 앞에서부터 순차적으로 한개씩 판단해서 최종 문자열을 만든다.
'''
import sys

input = sys.stdin.readline

S = input().strip()

result = ''
is_tag_open = False
word = ''

for char in S:
    if char in ['<', ' ']: # 단어가 끝난 경우, word를 뒤집어서 추가하고, 초기화한다.
        result += word[::-1] + char
        word = ''
    elif is_tag_open: # 태그가 열린상태인 경우, result에 바로 문자 추가
        result += char
    else: # 태그가 열린상태가 아닌 경우, word에 문자 추가
        word += char

    # 태그 열림 상태 변경
    if char == '<':
        is_tag_open = True
    elif char == '>':
        is_tag_open = False

result += word[::-1] # 마지막 단어를 뒤집어서 추가

print(result)