#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        results = []
        ints, ops = [], []
        i = j = 0
        
        while j < len(expression):
            if expression[j] == '+' or expression[j] == '-' or expression[j] == '*':
                ops.append(expression[j])
                ints.append(int(expression[i:j]))
                i = j + 1
            j += 1
        ints.append(int(expression[i:j]))
        
        def compute(ints, ops, start):
            if len(ints) <= 1:
                results.append(ints[0])
                return
            if start < 0:
                start = 0
            
            for i in range(start, len(ops)):
                if ops[i] == '+':
                    merged = ints[i] + ints[i + 1]
                elif ops[i] == '-':
                    merged = ints[i] - ints[i + 1]
                else:
                    merged = ints[i] * ints[i + 1]
                
                op = ops.pop(i)
                compute(ints[:i] + [merged] + ints[i + 2:], ops, i - 1)
                ops.insert(i, op)

        compute(ints, ops, -1)
        return results
# @lc code=end

