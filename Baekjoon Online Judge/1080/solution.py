import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix_A = [[int(num) for num in input().strip()] for _ in range(N)]
matrix_B = [[int(num) for num in input().strip()] for _ in range(N)]

# 뒤집는 작업은 두번 이상하는건 의미가 없다. 
# 각각의 부분 3x3 영역에 대해 뒤집지 않거나, 뒤집는 경우만 고려하면 된다.
# 하지만 각 단일 좌표의 입장에서는 여러번 뒤집힐 수 있으며, 짝수번 뒤집히면 원래 상태인거고, 홀수번 뒤집히면 바뀐 상태인 것이다.

# matrix_A[x][y]와 matrix_B[x][y]가 다르다는 것은 x, y에 뒤집는 작업이 홀수번 이뤄져야 한다는 것이다. 
# 좌상단부터 순차적으로 좌표를 한개씩 순회하고, x, y를 3x3 영역의 좌상단으로 설정하면,
# x, y 좌표의 값을 뒤집어야 한다면 반드시 지금 뒤집어야 하기 때문에 (지금 뒤집지 않으면 나중에 뒤집지 못함) 
# 그리디 형식으로 문제를 풀 수 있게 된다.

def count_min_operations():
    count = 0 # 3x3 영역을 뒤집은 횟수
    # 좌상단 좌표부터 우하단 좌표까지 순차적으로 순회한다.
    for x in range(N):
        for y in range(M):
            if x <= N - 3 and y <= M - 3: # 현재 좌표가 3x3 영역의 좌상단이 될 수 있다면
                if matrix_A[x][y] != matrix_B[x][y]:
                    count += 1
                    # 3x3 영역 뒤집기
                    for i in range(x, x + 3):
                        for j in range(y, y + 3):
                            matrix_A[i][j] = 0 if matrix_A[i][j] == 1  else 1
            else:
                if matrix_A[x][y] != matrix_B[x][y]: # 뒤집는 작업을 할 수 없는 좌표인데 뒤집어야 한다면
                    return -1
    return count

print(count_min_operations())