#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: list[int]) -> int:
        
        points = [0] 

        # 작은 로컬 웅덩이들의 물높이의 기준이 되는 기둥들의 위치를 points에 저장한다. 
        for i in range(1, len(height)):
            if height[i] >= height[i - 1]:  
                if points[-1] == i - 1:
                    points[-1] = i
                else:
                    points.append(i)

            while len(points) >= 3 and height[points[-2]] <= height[points[-3]] and height[points[-2]] <= height[points[-1]]:
                del points[-2]
        
        water = 0

        # 각각의 작은 웅덩이들의 물높이를 구했기 때문에 한번 순회해서 총 물 양을 구할 수 있다.
        if len(points) >= 2:
            for i in range(len(points) - 1):
                water_height = min(height[points[i]], height[points[i + 1]])
                for j in range(points[i] + 1, points[i + 1]):
                    if water_height > height[j]:
                        water += water_height - height[j]

        return water

        
                        
        
                

# @lc code=end

