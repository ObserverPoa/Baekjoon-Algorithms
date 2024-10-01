'''
곱의 합을 최소화하기 위해, A와 B를 서로 반대로 정렬해서 가장 작은 숫자가 가장 큰 숫자와 곱해지도록 한다.
'''
import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(sum(a * b for a, b in zip(sorted(A), sorted(B, reverse=True))))
