import string
import collections


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        ls = string.ascii_lowercase
        queue = collections.deque()
        queue.append([beginWord, 1])

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
