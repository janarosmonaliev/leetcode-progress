class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for column in range(len(text2)+1)]
              for row in range(len(text1)+1)]
        return 5


s = Solution()
text1 = "abcde"
text2 = "ace"
s.longestCommonSubsequence(text1, text2)
