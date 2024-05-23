class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = 0
        for i in range(k):
            current_sum += nums[i]
        
        pointer = k
        max_sum = current_sum
        while pointer < len(nums):
            current_sum-= nums[pointer-k]
            current_sum+= nums[pointer]
            max_sum = max(max_sum, current_sum)
            pointer+=1
        return max_sum / k


# Link: https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75
# Easy sliding window problem, self-explanatory