class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # keep track of max
        # amount = lower bar * distance between indices 
        # 2 pointers - at each end. measure amount, then increment whichever pointer is on lower bar. repeat until pointers equal each other 

        maximum = 0
        l = 0
        r = len(heights)-1

        while l != r:
            height = min(heights[l], heights[r])
            width = r - l
            amount = height * width
            maximum = max(maximum, amount)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maximum
        
        