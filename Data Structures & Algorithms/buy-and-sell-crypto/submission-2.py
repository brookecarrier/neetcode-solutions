class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of max 
        # 2 pointers, if prices[l]<prices[r], computer profit and increment r

        maximum = 0
        l = 0
        r = 1

        while r < len(prices):
            if l == r:
                r += 1
            elif prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maximum = max(maximum, profit)
                r += 1
            else:
                l += 1
        
        return maximum


      