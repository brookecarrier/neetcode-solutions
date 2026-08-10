class Solution:
    def climbStairs(self, n: int) -> int:

        def dfs(curr):
            if curr < 0:
                return 0
            if curr == 0:
                return 1
            return dfs(curr-1) + dfs(curr-2)


        return dfs(n)
        