class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 类比上楼梯问题，
        # dp[i]是凑齐价值为i需要的最少硬币数量
        # 首先将dp[i]设置为一个不可能的数

        dp = [0] + [float('inf') for _ in range(amount)]

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]
