from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      # array with one element case
      if len(nums) == 1:
        return nums[0]

      subarraySum = maxSum = nums[0]
      
      for i in range(1, len(nums)):
        subarraySum = max(nums[i], subarraySum+nums[i])
        
        if subarraySum > maxSum:
          maxSum = subarraySum
      
      return maxSum


s = Solution()
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(arr))