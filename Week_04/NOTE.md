题目：使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方

开始无序的地方就是这个数组中最小值的位置，所以问题可以等价为 [153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)

```python
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1

        while left < right:
            mid = (left+right)//2

            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid

        return nums[left]
```
