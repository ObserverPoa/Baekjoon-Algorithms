'''
1965번 문제의 풀이를 응용해서 해결할 수 있다.
이 문제 역시 최대 숫자가 1000 이고, O(n^2)에 풀 수 있다.
max_counts배열들의 원소를 -1로 초기화하는 것은, 자신을 포함하지 않기 때문이다.
모든 숫자에 대해 각각이 최대길이 바이토닉 부분수열의 Sk인 경우를 테스트 해본다.
max_len갱신을 위해서는, Sk에 대해 좌측과 우측에서 밖으로 갈수록 점점 작아지는 수열의 최대 길이가 필요하다.
그래서 x의 우측으로 갈 수록 점점 작아지는 숫자의 최대 개수를 right_max_counts[x][-1]에 미리 저장해두고,
다시 sequence의 왼쪽에서부터 순회하면서 left_max_counts[x]와 max_len을 한번에 갱신한다.
right_max_counts는 다시 되감을 수 있도록 스택을 사용헤서 히스토리를 남긴다.
'''
import sys

input = sys.stdin.readline

N = int(input())
sequence = list(map(int, input().split()))

right_max_counts = [[-1] for _ in range(1001)]
for num in reversed(sequence):
    right_max_counts[num].append(max(map(lambda x: x[-1], right_max_counts[:num])) + 1)


left_max_counts = [-1] * 1001
max_len = 0
for num in sequence:
    left_max_counts[num] = max(left_max_counts[:num]) + 1

    max_len = max(max_len, left_max_counts[num] + 1 + right_max_counts[num].pop())

print(max_len)
