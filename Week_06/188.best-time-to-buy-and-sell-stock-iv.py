class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        size = len(prices)

        # 一次交易由买入和卖出构成，至少需要两天。
        # 所以说有效的限制 k 应该不超过 n/2，如果超过，就没有约束作用了，相当于 k = +infinity。
        if k > size // 2:
            return self.helper(prices)

        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(size)]

        for i in range(size):
            for j in range(k, 0, -1):
                if i - 1 == -1:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue

                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[-1][k][0]

    def helper(self, prices):
        result = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                result += prices[i] - prices[i - 1]

        return result
