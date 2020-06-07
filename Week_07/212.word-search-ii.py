dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
END_OF_WORD = "#"


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # words 建立 Trie树
        # board DFS判定是否在树中

        if not board or not board[0]:
            return []
        if not words:
            return []
        self.m, self.n = len(board), len(board[0])
        self.result = set()

        root = {}
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node[END_OF_WORD] = END_OF_WORD

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self.dfs(board, i, j, "", root)

        return list(self.result)

    def dfs(self, board, i, j, cur_word, cur_dict):
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        if END_OF_WORD in cur_dict:
            self.result.add(cur_word)

        tmp, board[i][j] = board[i][j], '@'

        for k in range(4):
            x, y = dx[k] + i, dy[k] + j
            if 0 <= x < self.m and 0 <= y < self.n and board[x][y] != '@' and board[x][y] in cur_dict:
                self.dfs(board, x, y, cur_word, cur_dict)
        board[i][j] = tmp

        # root = {}
        # result, m, n = set(), len(board), len(board[0])
        # for word in words:
        #     node = root
        #     for char in word:
        #         node = node.setdefault(char, {})
        #     node['#'] = True
        #
        # def dfs(i, j, node, pre, visited):
        #     if '#' in node:
        #         result.add(pre)
        #     for (di, dj) in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        #         x, y = i + di, j + dj
        #         if 0 <= x < m and 0 <= y < n and board[x][y] in node and (x,y) not in visited:
        #             dfs(x, y, node[board[x][y]], pre + board[x][y], visited | {(x, y)})
        #
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] in root:
        #             dfs(i, j, root[board[i][j]], board[i][j], {(i, j)})
        # return list(result)

