# https://www.acmicpc.net/problem/14888

import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
opcodes = list(map(int, sys.stdin.readline().split()))

def operate(opcode, a, b):
    if opcode == 0:
        return a + b
    elif opcode == 1:
        return a - b
    elif opcode == 2:
        return a * b
    elif opcode == 3:
        if a < 0:
            return (a * -1 // b) * -1
        else:
            return a // b

max_result, min_result = None, None

def dfs(number, i, opcode):
    global max_result, min_result

    result = operate(opcode, number, numbers[i])

    if i == N - 1:
        max_result = result if max_result is None else max(result, max_result)
        min_result = result if min_result is None else min(result, min_result)

    for next_opcode, count in enumerate(opcodes):
        if count > 0:
            opcodes[next_opcode] -= 1
            dfs(result, i + 1, next_opcode)
            opcodes[next_opcode] += 1

dfs(0, 0, 0)

print(max_result)
print(min_result)