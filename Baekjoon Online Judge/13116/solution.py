'''
a, b의 루트노드까지의 공통 경로에 있는 노드 중 가장 큰 번호를 구한다. 
루트노드까지 노드 번호를 2로 나누면서 올라가는데, 
a, b 중 더 큰 수를 나눠서 두 수가 처음으로 같아지는 때를 찾는다.
'''
import sys

input = sys.stdin.readline

def M(a, b):
    while True:
        if a == b:
            return a
        if a > b:
            a //= 2
        elif a < b:
            b //= 2

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    k = M(A, B)
    print(k * 10)