class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp array of max up until i
        # either include i or start new seq

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        
        return max(dp)