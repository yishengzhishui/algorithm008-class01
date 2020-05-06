class Solution(object):
    def __init__(self):
        self.col, self.pie, self.na = [], [], []

    def solveNQueens(self, n):

        # the better code
        # def helper(queens, xy_diff, xy_sum):
        #     row = len(queens)
        #     if n == row:
        #         result.append(queens)
        #         return
        #
        #     for col in range(n):
        #         if col not in queens and col + row not in xy_sum and row-col not in xy_diff:
        #             helper(queens + [col], xy_diff + [row - col], xy_sum + [row + col]) # the + return the new list, do not change queens
        #
        # result = []
        # helper([], [], [])
        #
        # return [["."*i + "Q"+"."*(n-i-1) for i in sol] for sol in result]

        result = []
        self.dfs(n, result, [], 0)

        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in result]

    def dfs(self, n, result, s, row):
        if row == n:
            result.append(s)
            return

        for col in range(n):
            if col in self.col or col + row in self.pie or col - row in self.na:
                continue

            self.col.append(col)
            self.pie.append(col + row)
            self.na.append(col - row)

            self.dfs(n, result, s + [col], row + 1)

            self.col.remove(col)
            self.pie.remove(col + row)
            self.na.remove(col - row)