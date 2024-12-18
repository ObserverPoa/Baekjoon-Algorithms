'''
가로 길이가 짝수일때만 배치 가능하다.
3x2 영역에 배치하는 경우의 수는 3가지,
3x(4이상의 짝수) 영역에 배치하는 경우의 수는 2가지이다.

N이하의 짝수 가로길이 영역들의 합으로 N을 구성하는 모든 경우의 수를 구한다.
그걸 위해서, 먼저 가로길이 2로 완전히 분할한 상태에서 시작해서
i번째와 i+1번째를 병합하는 모든 경우의 수를 dfs로 탐색한다.
중복 탐색을 visited로 방지한다.
'''
import sys

input = sys.stdin.readline

N = int(input())

def count_cases(groups):
    cases = 1
    for group in groups:
        if group == 2:
            cases *= 3
        else:
            cases *= 2
    return cases

def dfs(groups, visited):
    key = '.'.join(map(str, groups))
    if key in visited: 
        return 0
    visited.add(key)

    cases = count_cases(groups)
    
    if len(groups) <= 1: 
        return cases

    for i in range(len(groups) - 1):
        cases += dfs(groups[:i] + [groups[i] + groups[i + 1]] + groups[i + 2:], visited)

    return cases


if N % 2 == 0:
    print(dfs([2] * (N // 2), set()))
else:
    print(0)
