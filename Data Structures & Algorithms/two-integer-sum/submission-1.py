class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numToIdx = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in numToIdx:
                j = numToIdx[complement]
                return [i, j] if i < j else [j, i]
            
            numToIdx[num] = i;
        
        return []
        