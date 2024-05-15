import re
class Solution:
    def reverseWords(self, s: str) -> str:
        pattern = r"\s*(\w+)\s*"
        result = re.findall(pattern, s)
        return " ".join(result[::-1])
    
    # Found this 90th percentile 1-liner, terrible readability
    def reverseWords2(self, s: str) -> str:
        return ' '.join(reversed(list(filter(lambda x: x != '', s.split(' ')))))
    

# Link: https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75
# Simple string regex question