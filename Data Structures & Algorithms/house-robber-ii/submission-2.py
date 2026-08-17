class Solution:
    def rob(self, nums: List[int]) -> int:
        # get max without last house
        # get max without first house
        # return max of the 2

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp_excludeFirst = [0] * (len(nums))
        dp_excludeFirst[1] = nums[1]
        dp_excludeFirst[2] = max(nums[1], nums[2])

        dp_excludeLast = [0] * (len(nums)-1)
        dp_excludeLast[0] = nums[0]
        dp_excludeLast[1] = max(nums[0], nums[1])        

        for i in range(3, len(nums)):
            dp_excludeFirst[i] = max(dp_excludeFirst[i-2] + nums[i], dp_excludeFirst[i-1])
        
        for i in range(2, len(nums)-1):
            dp_excludeLast[i] = max(dp_excludeLast[i-2] + nums[i], dp_excludeLast[i-1])
        
        return max(dp_excludeFirst[-1], dp_excludeLast[-1])