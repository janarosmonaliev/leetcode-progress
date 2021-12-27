from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # if list has more than 1 item and # of shifts isn't zero
        if len(nums) > 1 and k % len(nums) > 0:
            shift = k % len(nums)
            # buffer since we modify in-place
            temp = nums[:len(nums) - shift]
            nums[0:shift] = nums[-(shift):]
            nums[shift:] = temp
        return


s = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
s.rotate(nums, k)
print(nums)
