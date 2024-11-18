import sys

input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
op_counter = list(map(int, input().split()))

def are_sign_equal(x, y):
    return (x > 0 and y > 0) or (x < 0 and y < 0)

calculators = [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y,
    lambda x, y: x // y if are_sign_equal(x, y) else -(abs(x) // abs(y))
]

min_result = float('inf')
max_result = float('-inf')

# 매번 남은 연산자 중 한개를 사용하는 dfs
# result: 피연산자 x
# num_idx: 피연산자 y 인덱스
def dfs(result, num_idx):
    global min_result, max_result
    if num_idx == N:
        min_result = min(min_result, result)
        max_result = max(max_result, result)
        return
    
    num = numbers[num_idx] # 피연산자 y
    for i in range(4):
        if op_counter[i] > 0: 
            op_counter[i] -= 1
            dfs(calculators[i](result, num), num_idx + 1)
            op_counter[i] += 1

dfs(numbers[0], 1)

print(max_result)
print(min_result)

