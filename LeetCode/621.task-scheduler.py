\

# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
import collections, heapq
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        cur_time = 0
        waiting_queue = collections.deque()
        task_queue = []
        for task, count in collections.Counter(tasks).items():
            heapq.heappush(task_queue, (-count, task))

        # 가능한것 중에 가장 많이 남은 것을 우선으로 수행. 가능한 것이 없을 경우에는 IDLE.
        while waiting_queue or task_queue: 
            # 실행 가능한 시간이 된 작업들을 waiting queue에서 task queue로 이동시킨다.  
            while waiting_queue and cur_time > waiting_queue[0][0] + n:
                _, count, task = waiting_queue.popleft()
                heapq.heappush(task_queue, (count, task))

            if task_queue:
                count, task = heapq.heappop(task_queue)
                if count + 1 < 0:
                    waiting_queue.append((cur_time, count + 1, task))

            cur_time += 1

        return cur_time

# @lc code=end

