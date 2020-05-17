class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_reach, step, end = 0, 0, 0

        for i in range(len(nums) - 1):
            if i > max_reach:
                break

            max_reach = max(max_reach, i + nums[i])

            if i == end:
                end = max_reach
                step += 1

        return step
