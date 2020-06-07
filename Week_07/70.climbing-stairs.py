class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 递归+记忆
        if n == 1:
            return 1
        dic = [-1 for i in range(n)]
        dic[0], dic[1] = 1, 2
        return self.dfs(n - 1, dic)

    def dfs(self, n, dic):
        if dic[n] < 0:
            dic[n] = self.dfs(n - 1, dic) + self.dfs(n - 2, dic)
        return dic[n]

        # 动态规划
        # if n ==1:
        #     return 1
        # result = [0 for i in range(n)]
        # result[0], result[1] = 1,2
        # for i in range(2,n):
        #     result[i] = result[i-1]+result[i-2]
        # return result[-1]

        # 斐波那契数
        # f1, f2 = 1, 2
        # if n ==1:
        #     return f1
        # for i in range(2,n):
        #     f3 = f1 + f2
        #     f1 = f2
        #     f2 = f3
        #
        # return f2

        # a, b = 1, 1
        #
        # for i in range(n):
        #     a, b = b, a+b
        # return a
