'''
첫 daldidalgo를 입력하는데에 8초가 걸리고, 마지막 n을 입력하는데 1초가 걸려서, 9초는 최소 값이다.
N이 3이상일 떄, 마지막 N번째 daldidalgo 뒤에 daldida까지 붙여서 한번에 입력 가능하다.
daldia가 daldidalgo의 접두사이기 때문
그래서 마지막의 daldida 를 입력하는 것도 남은 입력해야 하는 반복 개수에 포함한다.
'''
import sys

input = sys.stdin.readline

N = int(input())

seconds = 9
max_repeat_count = 1 # 붙여넣을 수 있는 daldidalgo 반복 문자열의 최대 반복 길이
repeats_left = N # 남은 입력해야 하는 반복 개수

while repeats_left > 0:
    repeat_count = min(max_repeat_count, repeats_left)
    max_repeat_count += repeat_count
    repeats_left -= repeat_count
    seconds += 1

print(seconds)