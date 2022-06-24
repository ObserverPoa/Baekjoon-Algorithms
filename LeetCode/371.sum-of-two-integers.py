#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        sum = 0
        carry = 0
        for i in range(32):
            mask = 2 ** i
            A = a & mask
            B = b & mask

            sum |= A ^ B ^ carry
            carry = ((A & B) | (A & carry) | (B & carry)) << 1

        # 합이 음수일 경우, 32번째 이상 자리수를 모두 1로 채운다.
        if sum & (2 ** 31):
            sum |= -1 << 32

        return sum


# @lc code=end

