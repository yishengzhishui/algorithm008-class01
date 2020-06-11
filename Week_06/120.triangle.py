class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # F[i][j] = triangle[i+1][j]+triangle[i+1][j+1]

        # recursive + cache
        # size = len(triangle)
        # @functools.lru_cache(None)
        # def helper(x,y):
        #     if x == size -1:
        #         return triangle[x][y]
        #     left = helper(x+1,y)
        #     right = helper(x+1,y+1)
        #     return min(left,right)+triangle[x][y]
        #
        # return helper(0,0)

        # DP two-dimensional array
        # if not triangle:
        #     return  0
        # for i in range(len(triangle)-2, -1, -1):
        #     for j in range(len(triangle[i])):
        #         triangle[i][j] = min(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j]
        #
        # return triangle[0][0]

        # DP one-dimensional array
        # if not triangle:
        #     return  0
        #
        # result = triangle[-1]
        #
        # for i in range(len(triangle)-2, -1,-1):
        #     for j in range(len(triangle[i])):
        #         result[j] = min(result[j], result[j+1])+triangle[i][j]
        #
        # return result[0]
