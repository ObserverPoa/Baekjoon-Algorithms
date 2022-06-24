#
# @lc app=leetcode id=393 lang=python3
#
# [393] UTF-8 Validation
#

# @lc code=start
class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        mask234 = 0b10000000

        i = 0
        while i < len(data):
            # check first byte
            if data[i] ^ 0b00000000 < 0b10000000:
                pass
            elif data[i] ^ 0b11000000 < 0b100000:
                if i + 1 < len(data):
                    for _ in range(1):
                        i += 1
                        if data[i] ^ mask234 >= 0b1000000:
                            return False
                else:
                    return False
            elif data[i] ^ 0b11100000 < 0b10000 :
                if i + 2 < len(data):
                    for _ in range(2):
                        i += 1
                        if data[i] ^ mask234 >= 0b1000000:
                            return False
                else:
                    return False
            elif data[i] ^ 0b11110000 < 0b1000: 
                if i + 3 < len(data):
                    for _ in range(3):
                        i += 1
                        if data[i] ^ mask234 >= 0b1000000:
                            return False
                else:
                    return False
            else:
                return False

            i += 1

        return True
# @lc code=end

