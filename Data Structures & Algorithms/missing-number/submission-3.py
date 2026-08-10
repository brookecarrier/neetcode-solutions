class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)

        expected = (n + 1) * (n//2)
        if n % 2 != 0:
            expected += (n//2)+1
        
        return expected - total
        
        