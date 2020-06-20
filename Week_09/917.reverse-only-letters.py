class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """

        # # stack
        # stack, result = [], []
        #
        # #shorter stack = [s for s in S if s.isalpha()]
        #
        # for s in S:
        #     if s.isalpha():
        #         stack.append(s)
        #
        #
        # for i in S:
        #     if i.isalpha():
        #         result.append(stack.pop())
        #     else:
        #         result.append(i)
        #
        # return "".join(result)

        # 双指针 交换
        S = list(S)
        i, j = 0, len(S) - 1

        while i < j:
            if not S[i].isalpha():
                i += 1
            elif not S[j].isalpha():
                j -= 1
            else:
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1
        return "".join(S)

        # 反转指针

        # result = []
        # j = len(S) -1
        #
        # for i in S:
        #     if i.isalpha():
        #         while not S[j].isalpha():
        #             j -= 1
        #
        #         result.append(S[j])
        #         j -= 1
        #     else:
        #         result.append(i)
        #
        # return "".join(result)
