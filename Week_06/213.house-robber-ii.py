class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 第一家和最后一家，只能偷一家，其他的和198题目一致
        # a[i]: 0..1 nums[i]是必偷时，能够偷到的最大值，结果返回 max(a)

        # a[i] = max(a[i-1]+0, a[i-2]+nums[i])
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        size = len(nums)
        a = [0 for _ in range(size)]
        a[0] = nums[0]
        a[1] = max(nums[0], nums[1])

        for i in range(2, size):
            a[i] = max(a[i - 1], a[i - 2] + nums[i])

        return a[-1]
