class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, nums[i]+i)

        return True



        # reach = len(nums) -1
        #
        # for i in range(reach,-1,-1):
        #     if nums[i] +i >= reach:
        #         reach = i
        #
        # return reach == 0

        # another
        # max_i = 0  # 初始化当前能到达最远的位置
        # for i, jump in enumerate(nums):  # i为当前位置，jump是当前位置的跳数
        #     if i <= max_i < i + jump:  # 如果当前位置能到达，并且当前位置+跳数>最远位置
        #         max_i = i + jump  # 更新最远能到达位置
        # return max_i >= i

