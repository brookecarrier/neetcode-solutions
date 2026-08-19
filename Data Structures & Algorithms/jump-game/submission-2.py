class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # keep track of farthest possible jump
        # if i > farthest, false

        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False
            
            farthest = max(farthest, i + nums[i])
        
        return True