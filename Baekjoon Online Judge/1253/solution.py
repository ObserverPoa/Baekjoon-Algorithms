'''
N이 최대 2000 이므로, 완전 탐색을 할 수 있다.
수의 위치가 다르면 값이 같아도 다른 수이므로, counter를 사용해서 good여부를 한번에 카운팅한다.
'''
import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
number_counter = Counter(numbers)

good_number_count = 0
for i in range(N):
    for j in range(i + 1, N):
        number_sum = numbers[i] + numbers[j]

        # 0 + 0 = 0의 경우, 자신 이외의 것으로 만드려면 최소 3개는 있어야 한다.
        if numbers[i] == 0 and numbers[j] == 0 and number_counter[number_sum] < 3: continue

        # 0 + x = x의 경우, 자신 이외의 것으로 만드려면 최소 2개는 있어야 한다.
        if (numbers[i] == 0 or numbers[j] == 0) and number_counter[number_sum] < 2: continue

        good_number_count += number_counter[number_sum]

        # 한 숫자를 만드는 방법은 여러가지가 있을 수 있으므로, 중복 카운팅을 방지한다.
        number_counter[number_sum] = 0 

print(good_number_count)