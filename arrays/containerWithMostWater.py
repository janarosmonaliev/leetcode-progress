from curses.ascii import SO
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # there are 2 pointers, left and right
        left = 0
        right = len(height)-1
        area = 0

        # until left and right meet each other
        while left < right:
            # track the maximum area
            area = max(min(height[left], height[right]) * (right - left), area)

            # slide the shorter one
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return area


s = Solution()
arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(s.maxArea(arr))
