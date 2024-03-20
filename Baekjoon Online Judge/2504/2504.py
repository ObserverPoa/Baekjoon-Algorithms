# https://www.acmicpc.net/problem/2504

import sys

brackets = {
    ')': ('(', 2),
    ']': ('[', 3),
}

opening_brackets = set(
    map(lambda x: x[0], brackets.values())
) 

def solution(bracket_str):
    stack = []
    bracket_calc_results = []
    depth = 0

    for char in bracket_str:
        if char in opening_brackets:
            depth += 1
            stack.append(char)
        elif char in brackets and stack:
            current_bracket = stack.pop()
            opening_bracket, value = brackets[char]
            if current_bracket != opening_bracket:
                return 0
            
            depth -= 1

            if bracket_calc_results:
                result, result_depth = bracket_calc_results.pop()
                if depth == result_depth:
                    bracket_calc_results.append([result + value, depth])
                elif depth == result_depth - 1:
                    if bracket_calc_results and bracket_calc_results[-1][1] == depth:
                        bracket_calc_results[-1][0] += result * value
                    else:
                        bracket_calc_results.append([result * value, depth])
                else:
                    bracket_calc_results.append([result, result_depth])
                    bracket_calc_results.append([value, depth])
            else:
                bracket_calc_results.append([value, depth])
        else:
            return 0

    if stack:
        return 0
    else:
        return sum(map(lambda x: x[0], bracket_calc_results))
    

bracket_str = sys.stdin.readline().strip()
answer = solution(bracket_str)
print(answer)