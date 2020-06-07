class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        # 1. 将边界上的以及和边界相连的'O'变成'#'
        # 2. 将所有的'O'变成'X'

        # DFS
        if not board or not board[0]:
            return []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if (i in [0, m - 1] or j in [0, n - 1]) and board[i][j] == 'O':
                    self.dfs(i, j, board)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'

    # def bfs(self, i,j,board):
    #     m,n = len(board), len(board[0])
    #     queue = collections.deque()
    #     queue.append([i,j])
    #     board[i][j] = '#'
    #
    #     while queue:
    #         i, j = queue.popleft()
    #         for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
    #             if 0<=x<m and 0<=y<n and board[x][y] == 'O':
    #                 board[x][y] = '#'
    #                 queue.append([x,y])

    # def dfs(self, i, j, board):
    #     if 0 > i or i >= len(board) or 0 > j or j >= len(board[0]) or board[i][j] != 'O':
    #         return
    #     board[i][j] = '#'
    #     for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
    #         self.dfs(x, y, board)

    # Union find

    #     if not board: return []
    #
    #     m, n = len(board), len(board[0])
    #     surround = [i for i in range(m*n+1)]
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] == 'O':
    #                 if i in [0, m-1] or j in [0, n-1]:
    #                     surround[i*n+j] = m*n
    #
    #                 if i>0 and board[i-1][j] == 'O':
    #                     self.union((i-1)*n+j, i*n+j, surround)
    #                 if j>0 and board[i][j-1] == 'O':
    #                     self.union(i*n+j-1, i*n+j, surround)
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if self.find(i*n+j, surround) != m*n:
    #                 board[i][j] = 'X'
    #
    #
    # def find(self,x, p):
    #     root = x
    #     while root != p[root]:
    #         root = p[root]
    #
    #     return root
    #
    # def union(self, a,b,p):
    #     p1 = self.find(a, p)
    #     p2 = self.find(b, p)
    #     if p1>p2:
    #         p[p2] = p1
    #     elif p2>p1:
    #         p[p1] = p2
