class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # find expected sum of 0...n 
        # sum all numbers
        # subtract to find missing num

        expected = 0
        actual = 0

        for i in range(len(nums)+1):
            expected += i
        
        for num in nums:
            actual += num
        
        missing = expected - actual
        return missing



        
        
        