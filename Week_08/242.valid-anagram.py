class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # sort
        # s = sorted(s)
        # t = sorted(t)
        #
        # return s==t

        # hash
        # dic1, dic2 = {}, {}
        #
        # for i in s:
        #     dic1[i] = dic1.get(i, 0) + 1
        #
        # for j in t:
        #     dic2[j] = dic2.get(j, 0) + 1
        #
        # return dic1 == dic2

        # count
        # if len(s) != len(t):
        #     return False
        #
        # se = set(s)
        #
        # for i in se:
        #     if s.count(i) != t.count(i):
        #         return False
        #
        # return True
