from typing import List

class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    size = len(nums)
  # if array is [n] or []
    if size == 0 or size == 1:
      return

    slot = 0
    # move non-zero elements to front
    for i in range(size):
      if nums[i] != 0:
        nums[slot] = nums[i]
        slot+=1
    # fill rest with zeros
    nums[slot:size] = [0] * (size-slot)

s = Solution()
arr = [0,0,3,0,12, 9, 0 ,0, 1]
s.moveZeroes(arr)
print(arr)


        