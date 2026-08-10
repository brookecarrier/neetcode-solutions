class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # do binary search on 2 sections
        
        # find pivot val
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        pivot = l

        def binarySearch(nums, target, l, r):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1


        result = binarySearch(nums, target, 0, pivot - 1)

        if result != -1:
            return result
        
        return binarySearch(nums, target, pivot, len(nums)-1)
    
   

        