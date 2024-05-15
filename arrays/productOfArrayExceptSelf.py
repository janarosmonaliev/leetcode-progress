class Solution:
    # This solution is suboptimal, O(N) speed, O(N) space complexities
    def productExceptSelf(self, nums):
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        for idx in range(0, len(nums)):
            prefix[idx] = 1 if idx == 0 else prefix[idx - 1] * nums[idx - 1]

        for idx in reversed(range(len(nums))):
            postfix[idx] = (
                1 if idx == len(nums) - 1 else postfix[idx + 1] * nums[idx + 1]
            )
        return [prefix[i] * postfix[i] for i in range(len(nums))]
    
    # This solution is more optimized and uses O(1) space complexity
    def productExceptSelf2(self, nums):
        output = [1] * len(nums)
        right = 1

        for idx in range(1, len(nums)):
            output[idx] = output[idx - 1] * nums[idx - 1]

        for idx in reversed(range(len(nums)-1)):
            right = right * nums[idx + 1]
            output[idx] = right * output[idx]

        return output


