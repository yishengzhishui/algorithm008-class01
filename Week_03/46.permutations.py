class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # the library
        # result = []
        # for tmp in itertools.permutations(nums):
        #     result.append(tmp)
        #
        # return result

        # backtrack
        result = []
        self.helper(result, nums, [])
        return result

    def helper(self, result, nums, cur):
        if not nums:
            result.append(cur)
            return

        for i in range(len(nums)):
            self.helper(result, nums[:i] + nums[i + 1:], cur + [nums[i]])
