import functools


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # recursive up-bottom
        @functools.lru_cache(None)
        def helper(i, j):
            if i < 0 or j < 0:
                return 0
            if i == 0 or j == 0:
                return 1
            return helper(i - 1, j) + helper(i, j - 1)

        return helper(m - 1, n - 1)

        # dp = [[0 for _ in range(n)] for _ in range(m)]
        #
        # dp[0][0] = 1
        #
        # for x in range(m):
        #     for y in range(n):
        #         if x -1 >= 0:
        #             dp[x][y] += dp[x-1][y]
        #         if y-1>=0:
        #             dp[x][y] += dp[x][y-1]
        #
        #
        # return dp[-1][-1]

        # sample
        # dp = [[1 for _ in xrange(n)] for _ in xrange(m)]
        # for i in xrange(1, m):
        #     for j in xrange(1, n):
        #         dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # return dp[-1][-1]
