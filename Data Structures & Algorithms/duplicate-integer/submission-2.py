class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # check if nums[i] exists in hashmap
        # if so, return True
        # if not, add to map
        # return false after iterating thru nums

        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        
        return False
        