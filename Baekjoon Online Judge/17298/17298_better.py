n = int(input())

arr = list(map(int, input().split()))
ret = [-1] * n # 오큰수가 없다는걸 의미하는 값으로(-1) 결과 배열 초기화하고 시작

stack = [] # 수열의 index을 저장하는 stack
stack.append(0)

# 수열의 앞에서부터 탐색
# stack을 pop하면서 왼쪽의 원소들 중 현재의 원소가 오큰수인 index의 결과 배열에 현재 원소를 저장한다.
# 그 후 현재 원소의 index를 stack에 push해둔다
for idx in range(1, n):
    while stack and arr[stack[-1]] < arr[idx]:
        ret[stack.pop()] = arr[idx] # 현재 원소가 오큰수 일때까지 계속 pop
    stack.append(idx) # 현재 원소의 index를 stack에 저장 (추후에 현재 원소의 오큰수를 밝히기 위해)

# 이 시점에서 stack에는 오큰수가 없는 원소들의 index만 남아있게 된다.

print(*ret)