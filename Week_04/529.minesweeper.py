class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        # DFS
        if not board or not board[0]:
            return []

        i, j = click[0], click[1]

        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        direction = [[0, 1], [0, -1], [-1, 0], [1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        m, n = len(board), len(board[0])
        self.dfs(direction, i, j, board, m, n)
        return board

    def dfs(self, direction, i, j, board, m, n):
        if board[i][j] != 'E':
            return

        count = 0

        for x, y in direction:
            dx, dy = i + x, j + y

            if 0 <= dx < m and 0 <= dy < n and board[dx][dy] == 'M':
                count += 1

        if count == 0:
            board[i][j] = 'B'
        else:
            board[i][j] = str(count)
            return

        for x, y in direction:
            dx, dy = i + x, j + y

            if 0 <= dx < m and 0 <= dy < n:
                self.dfs(direction, dx, dy, board, m, n)
