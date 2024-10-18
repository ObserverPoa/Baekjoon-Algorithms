import sys

input = sys.stdin.readline

N = int(input())

W = [
    list(map(int, input().split()))
    for _ in range(N)
]

min_total_weight = float('inf')

# 완전탐색: O(N!)
def dfs(path, total_weight):
    global min_total_weight
    if len(path) == N:
        if W[path[-1]][path[0]] != 0:
            min_total_weight = min(min_total_weight, total_weight + W[path[-1]][path[0]])
        return
    
    for i in range(N):
        if i in path:
            continue
        if path and W[path[-1]][i] == 0:
            continue
        
        # 가지치기: 이미 최소 비용을 넘어선 경우
        weight = W[path[-1]][i] if path else 0
        if total_weight + weight >= min_total_weight:
            continue
        
        path.append(i)
        dfs(path, total_weight + weight)
        path.pop()
    

dfs([], 0)
print(min_total_weight)
