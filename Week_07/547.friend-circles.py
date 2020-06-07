class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # 并查集
        #     if not M:
        #         return 0
        #
        #     size = len(M)
        #     p = [i for i in range(size)]
        #
        #     for i in range(size):
        #         for j in range(size):
        #             if M[i][j] == 1:
        #                 self._union(p, i, j)
        #
        #     return len(set([self._parent(p, i) for i in range(size)]))
        #
        # def _union(self, p, i, j):
        #     p1 = self._parent(p, i)
        #     p2 = self._parent(p, j)
        #     p[p1] = p2
        #
        # def _parent(self, p, i):
        #     root = i
        #     while p[root] != root:
        #         root = p[root]
        #
        #     while p[i] != i:  # 路径压缩
        #         x = i
        #         i = p[i]
        #         p[x] = root
        #     return root

        # DFS

        if not M:
            return 0

        size = len(M)
        count, visited = 0, []
        for i in range(size):
            if i not in visited:
                self.dfs(M, visited, i)
                count += 1

        return count

    def dfs(self, M, visited, i):
        for j in range(len(M)):
            if M[i][j] == 1 and j not in visited:
                visited.append(j)
                self.dfs(M, visited, j)
