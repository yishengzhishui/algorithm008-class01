class Solution(object):
    def rotate(self, nums, k):
        length = len(nums)
        k = k % length

        # basic method
        # nums[:] = nums[length-k:] + nums[:length-k]

        # for loop
        # for i in range(k):
        #     nums.insert(0, nums.pop())

        # 反转
        self.reverseList(nums, 0, length - 1)
        self.reverseList(nums, 0, k - 1)
        self.reverseList(nums, k, length - 1)

    def reverseList(self, nums, start, end):
        i, j = start, end

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        return nums
