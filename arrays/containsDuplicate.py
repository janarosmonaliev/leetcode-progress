from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      map = {}
      for number in nums:
        if number in map.keys():
          return True
        else:
          map[number] = 1
      return 
      
    def containsDuplicate2(self, nums: List[int]) -> bool:
      return len(set(nums)) != len(nums)

s = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
print(s.containsDuplicate2(nums))
