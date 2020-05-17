import collections, string


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []

        ls = string.ascii_lowercase
        wordList = set(wordList)
        layer = {beginWord: [[beginWord]]}

        while layer:
            new_layer = collections.defaultdict(list)

            for word in layer:
                if word == endWord:
                    return layer[word]

                for i in range(len(word)):
                    for c in ls:
                        new_word = word[:i]+c+word[i+1:]
                        if new_word in wordList:
                            new_layer[new_word] += [j + [new_word] for j in layer[word]]

            wordList -= set(new_layer.keys())
            layer = new_layer

        return []

        # tree, ls, wordList, size = collections.defaultdict(set), string.ascii_lowercase, set(wordList), len(beginWord)
        # if endWord not in wordList: return []
        #
        # found, begin_queue, end_queue, next_queue, rev = False, {beginWord}, {endWord}, set(), False
        # while begin_queue and not found:
        #     wordList -= set(begin_queue)
        #     for x in begin_queue:
        #         for y in [x[:i] + c + x[i + 1:] for i in range(size) for c in ls]:
        #             if y in wordList:
        #                 if y in end_queue:
        #                     found = True
        #                 else:
        #                     next_queue.add(y)
        #                 tree[y].add(x) if rev else tree[x].add(y)
        #     begin_queue, next_queue = next_queue, set()
        #     if len(begin_queue) > len(end_queue):
        #         begin_queue, end_queue, rev = end_queue, begin_queue, not rev
        #
        # def bt(word):
        #
        #     if word == endWord:
        #         return [[word]]
        #
        #     return [[word] + rest for y in tree[word] for rest in bt(y)]
        #
        # return bt(beginWord)
