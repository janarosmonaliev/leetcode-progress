class Solution:
    # first solution with a hashmap where we iterate over the array twice
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap = dict()
        count = 0
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num] = 1
        
        for num in nums:
            if hashmap[num] >= 1 and k-num in hashmap and hashmap[k-num] >= 1:
                if num == k-num and hashmap[num] < 2:
                    continue
                hashmap[num]-=1
                hashmap[k-num]-=1
                count+=1
        return count
    
    # second solution with hashmap but with only 1 iteration
    def maxOperations2(self, nums: list[int], k: int) -> int:
        hashmap = dict()
        count = 0
        for num in nums:
            if k-num in hashmap and hashmap[k-num] > 0:
                count+=1
                hashmap[k-num]-=1
            elif num in hashmap:
                hashmap[num]+= 1
            else:
                hashmap[num] = 1
        return count