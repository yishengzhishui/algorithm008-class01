class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP 因为存在负数，负负得正，所以需要维护一个最小值
        # dp[i][0]max, dp[i][1]min
        # size = len(nums)
        # dp = [[1, 1] for i in range(size)]
        # dp[0][0] = dp[0][1] = result = nums[0]
        #
        # for i in range(1,size):
        #     if nums[i] < 0:
        #         dp[i-1][0], dp[i-1][1] = dp[i-1][1], dp[i-1][0]
        #
        #     dp[i][0] = max(dp[i - 1][0] * nums[i], nums[i])
        #     dp[i][1] = min(dp[i - 1][1] * nums[i], nums[i])
        #     result = max(result, dp[i][0])
        #
        # return result

        # DP 本元素的结果只和前一个元素有关

        size = len(nums)
        imax = imin = result = nums[0]
        for i in range(1, size):
            if nums[i] < 0:
                imax, imin = imin, imax

            imax= max(imax*nums[i], nums[i])
            imin= min(imin*nums[i], nums[i])
            result = max(imax, result)
        return result
