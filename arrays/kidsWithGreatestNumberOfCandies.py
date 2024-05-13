class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return map(lambda candy: candy + extraCandies >= max_candies, candies)

# Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# simple mapping approach