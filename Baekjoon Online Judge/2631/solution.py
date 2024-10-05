'''
최장 부분 증가 수열의 길이를 계산한다.
최장 부분 증가 수열의 숫자들은 움직이지 않아도 되는 숫자들이다.
결국 답은 N - max(max_increasing_lens) 으로 구할 수 있다.
'''
import sys

input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]

max_increasing_lens = [0] * 201 # KIS

for num in numbers:
    max_increasing_lens[num] = max(max_increasing_lens[:num]) + 1

print(N - max(max_increasing_lens))


