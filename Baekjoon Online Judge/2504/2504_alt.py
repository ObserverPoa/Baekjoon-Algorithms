# https://www.acmicpc.net/problem/2504

import sys

brackets = {
    ')': '(',
    ']': '[',
}

bracket_values = {
    '(': 2,
    '[': 3,
}

def solution(bracket_str):
    stack = []
    bracket_values_sum = 0
    bracket_value_product = 1
    is_opened_recently = False

    for char in bracket_str:
        if char in bracket_values:
            is_opened_recently = True
            bracket_value_product *= bracket_values[char]
            stack.append(char)
        elif char in brackets and stack:
            current_bracket = stack.pop()
            opening_bracket = brackets[char]
            if current_bracket != opening_bracket:
                return 0
            
            if is_opened_recently:
                is_opened_recently = False
                bracket_values_sum += bracket_value_product
            
            bracket_value_product //= bracket_values[opening_bracket]
        else:
            return 0

    if stack:
        return 0
    else:
        return bracket_values_sum
    

bracket_str = sys.stdin.readline().strip()
answer = solution(bracket_str)
print(answer)