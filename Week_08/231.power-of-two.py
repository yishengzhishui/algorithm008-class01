class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # n的二进制位有且仅有一个1
        return n != 0 and n & (n - 1) == 0
