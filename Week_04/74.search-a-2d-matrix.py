class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2

            num = matrix[mid // n][mid % n]

            if num == target:
                return True

            if num > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
