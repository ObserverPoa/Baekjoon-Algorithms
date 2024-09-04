'''
N이하의 연속적인 자연수의 합이 N이 되는 경우들을 찾아야 하므로,
슬라이딩 윈도우를 활용한다.
1부터 시작해서,
현재 연속된 수열의 합이 N보다 작은 경우에는 오른쪽에 다음으로 큰 숫자를 추가시키고,
N보다 큰 경우에는 윈도우의 가장 왼쪽의 숫자를 뺸다.
'''
import sys

input = sys.stdin.readline

N = int(input())

left, right = 1, 1
current_sum = 1
count = 0

# N의 절반보다 큰 숫자들로는 연속된 숫자의 합으로 N을 만들 수 없다.
while right <= N // 2 + 1 and right < N:
    if current_sum == N:
        count += 1
        right += 1
        current_sum += right
    elif current_sum < N:
        right += 1
        current_sum += right
    else:
        current_sum -= left
        left += 1

print(count + 1)


