class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        length = len(flowerbed)
        for i in range(1, length-1):
            if flowerbed[i-1] + flowerbed[i] + flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n-=1
            if n <= 0: return True
        return False
            

# Link https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75
# This solution iterates over the array and marks a spot as 1 
# if we can plant a flower there by checking adjacent plots.
# Note that algorithm prepends a 0 to the beginning and the end for easier iteration.

# Time complexity: O(N)
# Space complexity: O(1) ?
