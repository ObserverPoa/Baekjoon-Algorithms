'''
- 문제를 추가할 때, 같은 난이도의 경우 문제 숫자로 정렬될 수 있도록 튜플을 구성해서 우선순위 큐에 추가한다. 
- 문제를 추천할 때, 우선순위 큐에서 유효한 튜플이 나올때 까지 계속 pop한다.
'''
import sys
import heapq

input = sys.stdin.readline

difficulty_by_num = {} # 문제의 유효성 및 난이도를 조회하는 용도
min_pq = [] # min priority queue
max_pq = [] # max priority queue

# 문제를 시스템에 추가
def add_problem(num, difficulty):
    difficulty_by_num[num] = difficulty
    heapq.heappush(min_pq, (difficulty, num))
    heapq.heappush(max_pq, (-difficulty, -num))

# 문제를 시스템에서 삭제
def delete_problem(num):
    del difficulty_by_num[num]

# 가장 쉬운 문제번호들 중 가장 작은 번호 조회
def get_easiest_problem():
    while min_pq:
        difficulty, num = heapq.heappop(min_pq)
        if num in difficulty_by_num and difficulty_by_num[num] == difficulty:
            heapq.heappush(min_pq, (difficulty, num))
            return num

# 가장 어려운 문제번호들 중 가장 큰 번호 조회
def get_hardest_problem():
    while max_pq:
        difficulty, num = map(lambda x: -x, heapq.heappop(max_pq))
        if num in difficulty_by_num and difficulty_by_num[num] == difficulty:
            heapq.heappush(max_pq, (-difficulty, -num))
            return num

N = int(input())
for _ in range(N):
    num, difficulty = map(int, input().split())
    add_problem(num, difficulty)

M = int(input())
for _ in range(M):
    args = input().strip().split()

    if args[0] == 'recommend':
        if args[1] == '1':
            print(get_hardest_problem())
        elif args[1] == '-1':
            print(get_easiest_problem())
    elif args[0] == 'add':
        add_problem(int(args[1]), int(args[2]))
    elif args[0] == 'solved':
        delete_problem(int(args[1]))
