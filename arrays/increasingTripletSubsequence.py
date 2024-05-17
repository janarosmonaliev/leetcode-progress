class Solution:
    def increasingTriplet(self, nums) -> bool:
        first , second = 2**31 - 1, 2**31 - 1

        for num in nums:
            if num < first:
                first = num
            if num < second and num > first:
                second = num
            if num > second:
                
                return True
        return False


# Link: https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75
# Simple array traversal with use of 2 variables.