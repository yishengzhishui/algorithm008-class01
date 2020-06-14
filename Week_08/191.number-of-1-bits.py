class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # python bin函数
        # return bin(n).count('1')

        count = 0
        while n > 0:
            n = n & (n - 1)
            count += 1
        return count
