class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # DP方程：
        # dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
        # dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        if not prices:
            return 0
        max_k = 2
        size = len(prices)
        dp = [[[0,0] for _ in range(max_k+1)] for _ in range(size)]

        for i in range(size):
            for k in range(max_k, 0, -1):
                if i-1 == -1:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue

                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])


        return dp[-1][2][0]
