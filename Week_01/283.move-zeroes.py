class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # i = 0
        # for j in range(len(nums)):
        #     if nums[j] != 0:
        #         nums[i] = nums[j]
        #         i += 1
        # nums[i:] = [0] * (j - i +1)

        # 快排的思想
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
