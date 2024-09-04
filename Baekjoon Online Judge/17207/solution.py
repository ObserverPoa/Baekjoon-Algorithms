'''
난이도, 처리시간에 대한 2차원 행렬을 입력받고,
문제의 계산법대로 각 사람의 최종 일량을 계산하고, 
최종 일량이 가장 작은 사람들 중 번호가 가장 큰 사람의 이름을 출력한다.
'''
import sys

input = sys.stdin.readline

N = 5

# 번호 순서 이름 목록
names = ['Inseo', 'Junsuk', 'Jungwoo', 'Jinwoo', 'Youngki']

difficulties = [
    list(map(int, input().split())) for _ in range(N)
]

process_times = [
    list(map(int, input().split())) for _ in range(N)
]

# x번째 사람의 y번째 일의 예상 일량
def calc_workload(x, y):
    return sum([
        difficulties[x][i] * process_times[i][y] for i in range(N)
    ])

# 번호순 최종 일량 목록
total_workloads = [
    sum([
        calc_workload(x, y) for y in range(N)
    ]) for x in range(N)
]

min_num = 0 # 최종 일량이 가장 작은 사람들의 번호중 가장 큰 번호

for i in range(N):
    if total_workloads[i] <= total_workloads[min_num]:
        min_num = i

print(names[min_num])








