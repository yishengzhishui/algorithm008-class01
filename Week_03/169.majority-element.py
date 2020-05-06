class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort
        # nums.sort()
        # return nums[len(nums)//2]

        # divide and conquer
        # if not nums:
        #     return
        # if len(nums) == 1:
        #     return nums[0]
        #
        # a = self.majorityElement(nums[len(nums) // 2:])
        # b = self.majorityElement(nums[:len(nums) // 2])
        #
        # if a == b:
        #     return a
        #   # In Python 3.x True and False are keywords and will always be equal to 1 and 0.
        # return [b, a][nums.count(a) > len(nums) // 2]

        # hash count
        # cou = collections.Counter(nums)
        #
        # return max(cou.keys(), key=cou.get)

        # Boyer-Moore 投票算法
        count, cad = 0, None

        for n in nums:
            if count == 0:
                cad = n
            if cad == n:
                count += 1
            else:
                count -= 1

        return cad
