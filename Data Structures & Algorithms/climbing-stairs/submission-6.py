class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [n + 2] * (n + 2)
        dp[0], dp[1], dp[2] = 0, 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n] if (dp[n] != n + 2) else -1