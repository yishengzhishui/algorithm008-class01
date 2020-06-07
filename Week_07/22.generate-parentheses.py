class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.dfs(result, 0, 0, "", n)
        return result

    def dfs(self, result, left, right, cur, n):
        if right == n:
            result.append(cur)
            return

        if left < n:
            self.dfs(result, left + 1, right, cur + '(', n)

        if right < left:
            self.dfs(result, left, right + 1, cur + ')', n)
