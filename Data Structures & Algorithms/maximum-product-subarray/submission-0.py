class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxProduct = nums[0]

        if len(nums) == 1:
            return maxProduct
        
        for i in range(len(nums)):
            currProduct = nums[i]
            maxProduct = max(maxProduct, currProduct)
            for j in range(i+1, len(nums)):
                currProduct *= nums[j]
                maxProduct = max(maxProduct, currProduct)
        
        return maxProduct

  