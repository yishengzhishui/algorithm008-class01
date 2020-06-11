import functools


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # DP bottom-up
        if not text1 or not text2:
            return 0

        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        text1 = " " + text1
        text2 = " " + text2

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

        # recursive and lru_cache
        # @functools.lru_cache(None)
        # def helper(i,j):
        #     if i<0 or j <0:
        #         return 0
        #     if text1[i] == text2[j]:
        #         return helper(i-1, j-1) +1
        #     return max(helper(i-1,j), helper(i,j-1))
        # return helper(len(text1)-1, len(text2)-1)
