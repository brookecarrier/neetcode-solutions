class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # make set of all numbers
        # loop through elements
        # if element-1 DNE start a sequence
        # store max in var

        numsSet = set(nums)
        maxLen = 0
        currLen = 0


        for num in nums:
            if (num - 1) not in numsSet:
                currLen = 0
                currNum = num
                while (currNum in numsSet):
                    currLen += 1
                    currNum += 1
                maxLen = max(maxLen, currLen)
        
        return maxLen

        