class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1

        # while left <= right:
        #     mid = (left+right)/2
        #
        #     if target == nums[mid]:
        #         return mid
        #
        #     if nums[left] <= target < nums[mid] or nums[mid]<nums[0] <=target or target<nums[mid]<nums[0]:
        #         right = mid -1
        #     else:
        #         left = mid+1
        #
        # return -1

        while left < right:
            mid = (left+right)/2
            if (nums[0]>target) ^ (nums[0]> nums[mid]) ^ (target>nums[mid]):
                left = mid+1
            else:
                right = mid

        return left if target in nums[left:left+1] else -1
