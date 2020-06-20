import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # count = collections.Counter(s)
        #
        # for i, e in enumerate(s):
        #     if count[e] == 1:
        #         return i
        #
        # return -1

        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1

        for i, char in enumerate(s):
            if dic[char] == 1:
                return i
        return -1
