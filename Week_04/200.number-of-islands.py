import collections


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        count = 0
        if not grid:
            return count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    count += 1

        return count

    def bfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        queue.append([i, j])
        grid[i][j] = '#'

        while queue:
            i, j = queue.popleft()

            for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                    grid[x][y] = '#'

                    queue.append([x, y])

    # def dfs(self, grid, i, j):
    #     if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
    #         return
    #
    #     grid[i][j] = '#'
    #
    #     self.dfs(grid, i + 1, j)
    #     self.dfs(grid, i - 1, j)
    #     self.dfs(grid, i, j + 1)
    #     self.dfs(grid, i, j - 1)
