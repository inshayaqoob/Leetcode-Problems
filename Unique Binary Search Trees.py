class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 0:
            return 0
        
        # Create a DP array to store the number of unique BSTs for each number of nodes.
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        
        # Use dynamic programming to fill the DP array.
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        
        return dp[n]