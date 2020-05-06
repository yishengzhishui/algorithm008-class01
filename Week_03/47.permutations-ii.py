from collections import Counter


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def helper(counter, cur):
            if len(cur) == len(nums):
                result.append(cur)
                return

            for i in counter:
                if counter[i] > 0:
                    counter[i] -= 1
                    helper(counter, cur + [i])
                    counter[i] += 1

        result = []
        counter = Counter(nums)
        helper(counter, [])
        return result
