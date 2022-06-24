#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        brackets = []

        for char in s:
            if char in pairs:
                brackets.append(char)
            elif not brackets or pairs[brackets.pop()] != char:
                return False # 닫을 괄호가 없는데 닫으려고 하거나, 닫혀야 할 괄호와 쌍이 맞지 않는 경우
        
        # 열렸던 괄호가 전부 닫혔는지 확인
        return not brackets 

# @lc code=end

