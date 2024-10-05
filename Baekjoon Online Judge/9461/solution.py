'''
계속 오각형이 유지되면서 정삼각형을 붙여나가는 형태의 수열이다.
두 삼각형의 변이 이어져 한 변이 된 부분에 새롭게 붙인다.
P(n) = P(n-1) + P(n-5) 
'''
import sys

input = sys.stdin.readline

sequence = [1, 1, 1, 2, 2] # 초기값
for i in range(5, 100):
    sequence.append(sequence[i - 1] + sequence[i - 5])

T = int(input())
for _ in range(T):
    N = int(input())
    print(sequence[N - 1])

