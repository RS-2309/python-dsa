from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0

        while l < r:
            temp_area = min(height[l], height[r]) * (r - l)
            area = max(area, temp_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return area