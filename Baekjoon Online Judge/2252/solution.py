import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(list) # 작은 학생이 큰 학생을 가리키는 그래프
in_degree_counter = [0] * (N + 1) # 자신보다 작은 학생의 수

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree_counter[B] += 1


queue = deque()

for num in range(1, N + 1):
    count = in_degree_counter[num]
    if count == 0:
        queue.append(num)

# queue에는 아직 출력하지 않은 학생들 중에서 키가 가장 작다고 할 수 있는 학생들만 들어가 있다.
# 출력한 학생보다 큰 학생들의 (자신보다 작은 학생의 수)를 1 감소시키고,
# 자신보다 작은 학생의 수가 0이 된 학생을 queue에 추가한다.
while queue:
    num = queue.popleft()

    print(num, end=" ")

    for taller_num in graph[num]:
        in_degree_counter[taller_num] -= 1
        if in_degree_counter[taller_num] == 0:
            queue.append(taller_num)

