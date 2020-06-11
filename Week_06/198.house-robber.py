class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP: 1、重复子问题；2、状态的定义；3、DP方程
        # a[i]: 0..1 能够偷到 MAX Value，结果返回 a[-1]

        # a[i][0,1]: 0:i偷， 1:i不偷
        # a[i][0] = max(a[i-1][0], a[i-1][1])
        # a[i][1] = a[i-1][0] + nums[i]

        # if not nums:
        #     return 0
        #
        # size = len(nums)
        # a = [[0, 0] for i in range(size)]
        # a[0][0] = 0
        # a[0][1] = nums[0]
        #
        # for i in range(1,size):
        #     a[i][0] = max(a[i-1][0], a[i-1][1])
        #     a[i][1] = a[i-1][0] + nums[i]
        #
        # return max(a[-1][0], a[-1][1])


        # 优化：不增加新的维度

        # a[i]: 0..1 能够偷到 MAX Value，结果返回 max(a)
        # a[i]: 0..1,且nums[i]是必偷的最大值

        # a[i] = max(a[i-1]+0, a[i-2]+nums[i])

        if not nums:
            return 0
        size = len(nums)
        if size == 1 :
            return nums[0]

        a = [0 for i in range(size)]
        a[0] = nums[0]
        a[1] = max(nums[0], nums[1])

        for i in range(2, size):
            a[i] = max(a[i-1], a[i-2]+nums[i])

        return a[-1]
