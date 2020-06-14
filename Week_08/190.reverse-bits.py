class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        #取当前 n 的最后一位：n & 1
        #将最后一位移动到对应位置，第一次为 31 位，第二次是 30 位，即：31、30、29... 1、0

        result, power = 0, 31
        while n:
            result += (n&1) << power
            n = n>>1
            power -= 1

        return result
