class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        #
        # dp[0][0] = 1 - obstacleGrid[0][0]
        #
        # for i in range(m):
        #     for j in range(n):
        #         if obstacleGrid[i][j] == 1:
        #             dp[i][j] = 0
        #         else:
        #             if i > 0:
        #                 dp[i][j] += dp[i - 1][j]
        #
        #             if j > 0:
        #                 dp[i][j] += dp[i][j - 1]
        #
        # return dp[-1][-1]

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = 1 - obstacleGrid[0][0]

        for i in range(1,m):
            dp[i][0] = (1-obstacleGrid[i][0])*dp[i-1][0]

        for j in range(1,n):
            dp[0][j] = (1-obstacleGrid[0][j])*dp[0][j-1]

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0

                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]







        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        #
        # dp[m - 1][n - 1] = 1 - obstacleGrid[m - 1][n - 1]
        #
        # for x in range(m - 1, -1, -1):
        #     for y in range(n - 1, -1, -1):
        #         if obstacleGrid[x][y] == 1:
        #             dp[x][y] = 0
        #
        #         else:
        #             if x < m - 1:
        #                 dp[x][y] += dp[x + 1][y]
        #
        #             if y < n - 1:
        #                 dp[x][y] += dp[x][y + 1]
        #
        # return dp[0][0]

        # dp[m - 1][n - 1] = 1 - obstacleGrid[m - 1][n - 1]
        #
        # for j in range(n - 2, -1, -1):
        #     dp[m - 1][j] = dp[m - 1][j + 1] * (1 - obstacleGrid[m - 1][j])
        #
        # for i in range(m - 2, -1, -1):
        #     dp[i][n - 1] = dp[i + 1][n - 1] * (1 - obstacleGrid[i][n - 1])
        #
        # for x in range(m - 2, -1, -1):
        #     for y in range(n - 2, -1, -1):
        #         if obstacleGrid[x][y] == 1:
        #             dp[x][y] = 0
        #
        #         else:
        #             dp[x][y] = dp[x][y + 1] + dp[x + 1][y]
        #
        # return dp[0][0]

        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        # dp = [[0 for y in range(n)] for x in range(m)]

        # 自底向上
        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         if obstacleGrid[i][j] == 1:
        #             dp[i][j] = 0
        #
        #         else:
        #             if i == m-1 and j == n -1:
        #                 dp[i][j] = 1
        #             elif i == m -1:
        #                 dp[i][j] = dp[i][j+1]
        #             elif j == n-1:
        #                 dp[i][j] = dp[i+1][j]
        #             else:
        #                 dp[i][j] = dp[i+1][j] + dp[i][j+1]
        #
        # return dp[0][0]

        # 自顶向下
        # dp[0][0] = 1 - obstacleGrid[0][0]
        #
        # for i in range(1, m):
        #     dp[i][0] = dp[i - 1][0] * (1 - obstacleGrid[i][0])
        #
        # for j in range(1, n):
        #     dp[0][j] = dp[0][j - 1] * (1 - obstacleGrid[0][j])
        #
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) * (1 - obstacleGrid[i][j])
        #
        # return dp[-1][-1]
