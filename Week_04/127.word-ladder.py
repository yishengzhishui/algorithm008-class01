import collections, string


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        queue = collections.deque()
        queue.append([beginWord, 1])
        ls = string.ascii_lowercase
        wordList = set(wordList)

        while queue:
            cur, level = queue.popleft()

            if cur == endWord:
                return level

            for i in range(len(cur)):
                for e in ls:
                    word = cur[:i] + e + cur[i + 1:]
                    if word in wordList:
                        wordList.remove(word)
                        queue.append([word, level + 1])

        return 0

        # def construct_dict(word_list):
        #     d = {}
        #     for word in word_list:
        #         for i in range(len(word)):
        #             new_word = word[:i] + '_' + word[i+1:]
        #             d[new_word] = d.get(new_word, []) + [word]
        #
        #     return d
        #
        #
        # def bfs(begin, end, dic):
        #     queue = collections.deque()
        #     queue.append([begin, 1])
        #     visited = set()
        #
        #     while queue:
        #         word, step = queue.popleft()
        #         if word not in visited:
        #             visited.add(word)
        #             if word == end:
        #                 return step
        #
        #             for i in range(len(word)):
        #                 new_word = word[:i] +'_' + word[i+1:]
        #                 neigh_words = dic.get(new_word, [])
        #                 for neigh in neigh_words:
        #                     if neigh not in visited:
        #                         queue.append([neigh, step+1])
        #
        #     return 0
        #
        # dic = construct_dict(set(wordList))
        # return bfs(beginWord, endWord, dic)
