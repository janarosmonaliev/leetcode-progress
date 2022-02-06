from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # forward accumulation array
        # backwards accumulation array
        # [i] = forward[i-1] * backwards[i+1] except 1st and last

        forward = [0] * len(nums)
        backward = [0] * len(nums)

        # for i in range(len(nums)):
        # forward
        return []
