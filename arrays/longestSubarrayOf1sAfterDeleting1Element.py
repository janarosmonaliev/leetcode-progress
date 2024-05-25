class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 2 pointers problem
        left, right = 0, 0
        max_subarray = 0
        # to keep track whether the window is valid
        deletions = 1

        while right < len(nums):
            # if we encounter 0, imagine that we deleted it
            if nums[right] == 0: 
                deletions -= 1

            # if we deleted > 1 0s already, we need to shift the left pointer
            if deletions < 0:
                # keep track of this subarray of 1s
                max_subarray = max(max_subarray, right-left-1)
                # if left is 0, we give back deletions
                if nums[left] == 0:
                    deletions +=1
                left+=1
            right+=1
        # this covers edge cases of <=1 0s in array
        max_subarray = max(max_subarray, right-left-1)
        return max_subarray
    
    # Link: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=study-plan-v2&envId=leetcode-75
    