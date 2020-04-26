class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # if len(s) != len(t):
        #     return False
        #
        # dic1, dic2 = {}, {}
        #
        # for i in s:
        #     dic1[i] = dic1.get(i, 0) + 1
        #
        # for j in t:
        #     dic2[j] = dic2.get(j, 0) + 1
        #
        # return dic1 == dic2

        return sorted(s) == sorted(t)