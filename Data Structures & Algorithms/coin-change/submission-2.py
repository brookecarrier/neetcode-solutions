class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp array for min coins to make every number up to amount

        dp = [float('inf')] * (amount+1)

        # takes 0 coins to make $0
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        if dp[amount] == float('inf'): return -1

        return dp[amount]

        