class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0

        while right < len(nums):
            if nums[right] == 0: k-=1

            if k < 0:
                if nums[left] == 0: k+=1
                left+=1
            right+=1
        return right-left

# Link: https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75
# This is a sliding window problem where we expand the right pointer as long as the window is valid (0s to flip <= k).
# Once we run out of 0 to flip, we move the left pointer to the right and throw away 0s.