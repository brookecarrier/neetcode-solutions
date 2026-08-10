class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # put all nums in set 
        # for each num, see if the previous num exists in set
        # if not, find largest sequence w that as starting number
        
        nums_set = set(nums)
        longest = 0
        
        for num in nums:
            if num-1 not in nums_set:
                current = 1
                while num+1 in nums_set:
                    current += 1
                    num += 1
                
                longest = max(current, longest)
        
        return longest


        