'''
2차원 배열의 직사각형 영역의 합을 구한다.
(x1, y1)는 영역의 좌상단 좌표이고, (x2, y2)는 영역의 우하단 좌표이다.
'''
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [
    list(map(int, input().split())) for _ in range(N)
]

K = int(input())

def sum_area(x1, y1, x2, y2):
    return sum([
        sum([
           matrix[i][j] for j in range(y1, y2 + 1)
        ]) for i in range(x1, x2 + 1)
    ])

for _ in range(K):
    i, j, x, y = map(int, input().split())

    # zero based 넘버링으로 인덱스를 변환해서 합 계산
    print(sum_area(i - 1, j - 1, x - 1, y - 1)) 
    
