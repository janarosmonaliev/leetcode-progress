class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "": return True
        i, j = 0,0
        while i < len(t):
            if t[i] == s[j]:
                j+=1
            i+=1
            if j == len(s):
                return True
            
        return False
        

# Link: https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75
# Simple 2 Pointers solution, where we iterate over the main string, while checking the subsequent string.