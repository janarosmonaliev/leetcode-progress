class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_gain = 0
        altitude = 0
        for i in range(len(gain)):
            altitude+=gain[i]
            max_gain = max(altitude, max_gain)
        return max_gain

# Link: https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75
# Easy prefix problem