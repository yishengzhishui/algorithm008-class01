class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        # split reverse join
        return " ".join(reversed(s.split()))
