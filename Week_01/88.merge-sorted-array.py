class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # basic method
        # nums1[:] = nums1[:m] + nums2[:]

        # 双指针法，从前往后，需要额外的空间

        # nums1_copy = nums1[:m]
        # nums1[:] = []
        # i, j = 0, 0
        #
        # while i < m and j < n:
        #     if nums1_copy[i] < nums2[j]:
        #         nums1.append(nums1_copy[i])
        #         i += 1
        #     else:
        #         nums1.append(nums2[j])
        #         j += 1
        #
        # if i == m:
        #     nums1[i+j:] = nums2[j:]
        #
        # if j == n:
        #     nums1[i+j:] = nums1_copy[i:]


        # 双指针法，从前往后，不需要额外空间

        i, j, p = m-1, n-1, m+n-1

        while i >= 0 and j >= 0:
            if nums2[j] > nums1[i]:
                nums1[p] = nums2[j]
                j -= 1
            else:
                nums1[p] = nums1[i]
                i -= 1
            p -= 1

        if j>= 0:
            nums1[:j+1] = nums2[:j+1]

