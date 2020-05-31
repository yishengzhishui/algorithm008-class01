class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # basic dp
        # m, n = len(grid), len(grid[0])
        # dp = [[0 for _ in range(n)] for _ in range(m)]

        # for i in range(m - 1, -1, -1):
        #     for j in range(n - 1, -1, -1):
        #         if i == m - 1 and j == n - 1:
        #             dp[i][j] = grid[i][j]
        #         elif i == m - 1:
        #             dp[i][j] = grid[i][j] + dp[i][j + 1]
        #         elif j == n - 1:
        #             dp[i][j] = grid[i][j] + dp[i + 1][j]
        #         else:
        #             dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
        #
        # return dp[0][0]

        # faster
        # dp[m-1][n-1] = grid[m-1][n-1]
        # for i in range(m-2, -1, -1):
        #     dp[i][n-1] = grid[i][n-1] + dp[i+1][n-1]
        #
        # for j in range(n-2, -1, -1):
        #     dp[m-1][j] = grid[m-1][j] + dp[m-1][j+1]
        #
        # for i in range(m - 2, -1, -1):
        #     for j in range(n - 2, -1, -1):
        #         dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
        #
        # return dp[0][0]

        # change the grid itself
        m, n = len(grid), len(grid[0])
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]

        for x in range(1, m):
            for y in range(1,n):
                grid[x][y] += min(grid[x-1][y], grid[x][y-1])
        return grid[-1][-1]
