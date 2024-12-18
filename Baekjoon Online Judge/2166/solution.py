'''
신발끈 공식을 사용한다.
'''
import sys

input = sys.stdin.readline

def shoelace_formula(coords):
    sum1, sum2 = 0, 0
    for i in range(len(coords)):
        sum1 += coords[i][1] * coords[i - 1][0]
        sum2 += coords[i][0] * coords[i - 1][1]
    return abs(sum1 - sum2) / 2

N = int(input())

coords = [
    list(map(int, input().split())) 
    for _ in range(N)
]

area = shoelace_formula(coords)

print(round(area, 1))