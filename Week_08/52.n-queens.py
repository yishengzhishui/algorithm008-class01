class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        # simple code for N queens
        #     result = []
        #     self.dfs(result, [], [], [], n)
        #     return len(result)
        # def dfs(self, result, cur, xy_diff, xy_sum, n):
        #     row = len(cur)
        #     if row == n:
        #         result.append(cur)
        #         return
        #
        #     for col in range(n):
        #         if col not in cur and col + row not in xy_sum and col - row not in xy_diff:
        #             self.dfs(result, cur + [col], xy_diff + [col - row], xy_sum + [col + row], n)

        # 位运算

        if n < 1: return []
        self.count = 0
        self.DFS(n, 0, 0, 0, 0)
        return self.count

    def DFS(self, n, row, cols, pie, na):
        if row == n:
            self.count += 1
            return

        bits = (~(cols | pie | na)) & ((1 << n) - 1)  # 得到当前所有的空位， 空位为1

        while bits:
            p = bits & -bits  # 取到最低位的1, 1的位置没有被攻击的
            bits = bits & (bits - 1)  # 表示在p位置上放入皇后（最低位的1清零）
            self.DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
            # 不需要revert  cols, pie, na 的状态
