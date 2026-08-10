class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # prefix and suffix, [i] is product of the 2
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output
        