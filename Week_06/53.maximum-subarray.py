class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dp[i] 是到第i个为止，连续子数组最大的和,最后返回dp中的最大值
        # size = len(nums)
        # dp = [0 for _ in range(size)]
        # for i in range(size):
        #     dp[i] = max(dp[i-1]+nums[i], nums[i])
        #
        # return max(dp)

        # dp[i] 是到第i个为止，连续子数组最大的和, result的到最后的结果
        # if not nums:
        #     return None
        # size = len(nums)
        # dp = [0 for _ in range(size)]
        # result = nums[0]
        # for i in range(size):
        #     dp[i] = max(dp[i - 1] + nums[i], nums[i])
        #     result = max(dp[i], result)
        # return result

        if not nums:
            return None
        cur = result = nums[0]
        for i in range(1, len(nums)):
            cur = max(cur + nums[i], nums[i])
            result = max(cur, result)
        return result
