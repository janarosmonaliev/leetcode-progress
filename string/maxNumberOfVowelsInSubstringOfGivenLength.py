class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_count = 0
        j = k
        for i in range(k):
            if s[i] in vowels:
                max_count += 1
        count = max_count
        while j < len(s):
            if s[j] in vowels:
                count += 1
            if s[j-k] in vowels:
                count -= 1
            max_count = max(count, max_count)
            j+=1
        return max_count

# Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75
# Simple sliding window problem where we move the window while keeping track of max vowels