class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {i: 0 for i in range(128)}
        start = end = 0
        result = 0

        while end < len(s):
            c1 = ord(s[end])
            map[c1] += 1

            while map[c1] > 1:
                print(s[start:end])
                c2 = ord(s[start])
                map[c2] -= 1
                start += 1

            result = max(result, end-start+1)
            end += 1

        return result


s = Solution()
answer = s.lengthOfLongestSubstring('abcabcbb')
print(answer)
