class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        p2, p3, p5 = 0, 0, 0
        result = [1]

        for i in range(1, n):
            min_result = min(result[p2] * 2, result[p3] * 3, result[p5] * 5)
            if min_result == result[p2] * 2:
                p2 += 1

            if min_result == result[p3] * 3:
                p3 += 1

            if min_result == result[p5] * 5:
                p5 += 1

            result.append(min_result)

        return result[-1]
