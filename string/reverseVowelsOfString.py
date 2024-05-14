class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {vowel: 1 for vowel in list('aeiouAEIOU')}
        word = list(s)
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] in vowels:
                if s[end] in vowels:
                    word[start], word[end] = word[end], word[start]
                    end -= 1
                    start += 1
                else:
                    end -= 1
            else:
                start += 1
        return "".join(word)
               

# Link: https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75
# Simple 2 pointers question.