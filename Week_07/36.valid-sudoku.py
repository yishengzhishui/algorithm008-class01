class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # big = set()
        # for i in xrange(0, 9):
        #     for j in xrange(0, 9):
        #         if board[i][j] != '.':
        #             cur = board[i][j]
        #             if (i, cur) in big or (cur, j) in big or (i / 3, j / 3, cur) in big:
        #                 return False
        #             big.add((i, cur))
        #             big.add((cur, j))
        #             big.add((i / 3, j / 3, cur))
        # return True

        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if not board[i][j].isnumeric():
                    continue
                num = board[i][j]
                if (num in row[i]) or (num in col[j]) or (num in boxes[(i // 3) * 3 + j // 3]):
                    return False
                row[i].add(num)
                col[j].add(num)
                boxes[(i // 3) * 3 + j // 3].add(num)
        return True
