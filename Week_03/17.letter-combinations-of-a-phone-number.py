class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        # recursive

        # if not digits:
        #     return []
        #
        # if len(digits) == 1:
        #     return list(mapping[digits[0]])
        #
        # additional = mapping[digits[-1]]
        # pre = self.letterCombinations(digits[:-1])
        #
        # return [a+b for a in pre for b in additional]

        # backtrack
        if not digits:
            return []
        result = []

        self.dfs(digits, result, 0, mapping, '')

        return result

    def dfs(self, digits, result, index, mapping, s):
        if index == len(digits):
            result.append(s)
            return

        for i in mapping[digits[index]]:
            self.dfs(digits, result, index + 1, mapping, s + i)
