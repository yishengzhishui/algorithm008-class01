class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # DP + extra space
        # if not prices:
        #     return 0
        # size = len(prices)
        # dp = [[0, 0] for _ in range(size)]
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]
        # for i in range(1, size):
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        #
        # return dp[-1][0]


        # DP more simple
        if not prices:
            return 0

        size = len(prices)
        dp_0, dp_1 = 0, -prices[0]

        for i in range(1, size):
            tmp = dp_0
            dp_0 = max(dp_0, dp_1 + prices[i])
            dp_1 = max(dp_1, tmp - prices[i])
        return dp_0

        # 贪心算法
        # result = 0
        #
        # for i in range(1, len(prices)):
        #     if prices[i] > prices[i-1]:
        #         result += prices[i] - prices[i-1]
        #
        # return result
