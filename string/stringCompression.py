class Solution:
    def compress(self, chars) -> int:
        if len(chars) == 1:
            return 1
        
        i = 0 # primary iterator
        write_index = 0 # write index and count
        total_length = 0 # result

        while i < len(chars):
            j = 1 # secondary iterator
            while i + j < len(chars) and chars[i+j] == chars[i]:
                j+=1 # move iterator
                
            chars[write_index] = chars[i]
            write_index+=1
            if j > 1:
                for letter in str(j):
                    chars[write_index] = letter
                    write_index+=1
            i += j
        return write_index
    
# Link: https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75
# This is a 2 Pointers solution to the string compression problem.
# We have a 2 nested loops, where we iterate over internal one if letters repeat and update the outher loop iterator,
# otherwise, we just iterate over the outer loop and modify the input array. The time complexity is still O(N),
# space complexity is O(1).