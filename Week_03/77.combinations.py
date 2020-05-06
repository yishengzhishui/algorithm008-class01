class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        # library itertools
        # result = []
        # for tmp in itertools.combinations(range(1, n+1), k):
        #     result.append(tmp)
        #
        # return result

        # backtrack
        def helper(cur, start):
            if len(cur) == k:
                result.append(cur)
                return

            for i in range(start, n + 1):
                helper(cur + [i], i + 1)

        result = []
        helper([], 1)
        return result
