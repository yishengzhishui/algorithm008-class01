class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # dp[i][j] s[i][j]是否是回文串
        # 空的或长度为1的子串是回文串
        # dp[i][j] = dp[i+1][j-1] and  s[i] == s[j]

        size = len(s)
        res = ""
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]

        # for i in range(size - 1, -1, -1):
        #     for j in range(i, size): # i是起点，j是终点j再i的后面, 一步一步遍历所有的元素
        #         dp[i][j] = s[i] == s[j] and (j-i < 2 or dp[i + 1][j - 1])
        #
        #         #输出当前 更长 的回文串
        #         if dp[i][j] and j-i + 1 > len(res):
        #             res = s[i:j + 1]
        # return res

        for j in range(size):
            for i in range(j, -1, -1):

                dp[i][j] = s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1])

                # 输出当前 更长 的回文串
                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j + 1]
        return res
