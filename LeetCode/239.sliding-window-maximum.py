#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
import heapq, collections

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # window = collections.defaultdict(int)
        # queue = []
        # for i in range(k - 1):
        #     heapq.heappush(queue, -nums[i])
        #     window[nums[i]] += 1

        # result = []

        # left = 0
        # for right in range(k - 1, len(nums)):
        #     heapq.heappush(queue, -nums[right])
        #     window[nums[right]] += 1

        #     while window[-queue[0]] <= 0:
        #         heapq.heappop(queue)

        #     result.append(-queue[0])
            
        #     window[nums[left]] -= 1 
        #     left += 1

        # return result

        deq, ans = collections.deque(), []

        for i in range(len(nums)):
            # 뒤에서부터 현재 추가할 숫자보다 작으면 -> 제거 (deq에 불필요한 숫자 없도록!)
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()
            
            deq.append(i) # 현재 숫자 추가( (i, num[i])로 저장해도 되나, 숫자 위치 저장만 해 space 줄임)

            # 앞에서부터 out of window -> 제거
            if i - deq[0] == k:
                deq.popleft()

            # 출력 부분 (현재 위치 >= window size일 때)
            if i + 1 >= k:
                ans.append(nums[deq[0]])  # 맨 앞은 현재 window 에서 가장 큰 수

        return ans



# @lc code=end

