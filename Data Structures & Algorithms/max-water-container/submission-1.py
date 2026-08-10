class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxAmount = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            if heights[l] <= heights[r]:
                currAmount = heights[l] * (r - l)
                l += 1
            else:
                currAmount = heights[r] * (r - l)
                r -= 1
            maxAmount = max(maxAmount, currAmount)
        
        return maxAmount
            

        