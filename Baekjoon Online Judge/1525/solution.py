'''
빈칸으로 부터 탐색을 시작해서, 인접한 칸과 스왑해나가는 모든 경우의 수를 탐색한다.
현재까지 확인한 표의 상태중 한개로 다시 되돌아왔을 경우, 해당 탐색 가지는 중지한다.
완전히 정리된 상태가 될 때까지 탐색을 계속한다. 각 표 상태마다 최소 이동 횟수 (스왑 횟수)를 기록한다.
'''
import sys
from collections import deque

input = sys.stdin.readline

N = 3

initial_table = ''.join([ ''.join(input().split()) for _ in range(N) ])

def is_valid_coord(x, y):
    return 0 <= x < N and 0 <= y < N

def create_swapped(table: str, x1, y1, x2, y2):
    table_items = list(table)
    table_items[N * x1 + y1], table_items[N * x2 + y2] = table_items[N * x2 + y2], table_items[N * x1 + y1]
    return ''.join(table_items)

def find_zero_coord(table: str):
    return divmod(table.find('0'), N)

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

TARGET_TABLE = "123456780"

visited_tables = set()

def bfs(start_table):
    queue = deque([(start_table, *find_zero_coord(start_table), 0)])
    visited_tables.add(start_table)

    while queue:
        table, x, y, moves = queue.popleft()

        if table == TARGET_TABLE:
            return moves

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not is_valid_coord(nx, ny): continue

            next_table = create_swapped(table, x, y, nx, ny)
            if next_table in visited_tables: continue

            visited_tables.add(next_table)
            queue.append((next_table, nx, ny, moves + 1))

    return -1

print(bfs(initial_table))
