class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # one pointer, iterate thru array
        # check if complement (target - nums[i]) exists
            # if it does, return (complement index, i)
            # if it doesn't, add nums[i] to map

        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            else:
                hashmap[nums[i]] = i


        