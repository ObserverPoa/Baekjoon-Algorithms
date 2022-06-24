#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        orig_counter = collections.Counter(t)

        window = collections.deque()
        cur_counter = collections.defaultdict(int)
        cur_len = 0

        min_substr = ''

        for char in s:
            # 슬라이딩 윈도우 우측에 한개 추가
            window.append(char)
            if char in orig_counter:
                cur_counter[char] += 1
                cur_len += cur_counter[char] <= orig_counter[char]
            
            # 현재 슬라이딩 윈도우가 substr의 조건을 만족하는 경우
            if cur_len == len(t):
                # 슬라이딩 윈도우의 왼쪽을 제거 가능할때까지 제거.
                while window:
                    front = window[0]
                    if front not in orig_counter:
                        window.popleft()
                    elif cur_counter[front] > orig_counter[front]:
                        cur_counter[window.popleft()] -= 1
                    else:
                        break

                if not min_substr or len(window) < len(min_substr):
                    min_substr = ''.join(window)

                # 새로운 minimum substr을 찾기 위해, 슬라이딩 윈도우 왼쪽 한개 제거
                popped = window.popleft()
                if popped in orig_counter:
                    cur_counter[popped] -= 1
                    cur_len -= cur_counter[popped] < orig_counter[popped]


        return min_substr

# @lc code=end

