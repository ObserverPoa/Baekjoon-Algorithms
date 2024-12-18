import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

coins = set([int(input()) for _ in range(n)])

# bfs  
# 0부터 동전을 종류별로 더하는 경우를 k가 될때까지 반복한다.
def count_min_coin():
    queue = deque([(0, 0)])
    visited = set([0])

    while queue:
        total_sum, used_count = queue.popleft() # 동전 합, 사용 동전 개수

        next_used_count = used_count + 1

        for coin in coins:
            next_total_sum = total_sum + coin
            if next_total_sum > k:
                continue
            elif next_total_sum == k:
                return next_used_count
            elif next_total_sum not in visited:
                visited.add(next_total_sum)
                queue.append((next_total_sum, next_used_count))
    return -1

print(count_min_coin())        
