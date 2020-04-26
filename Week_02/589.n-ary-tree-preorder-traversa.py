class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        # recursive

        # if not root:
        #     return []
        #
        # result = [root.val]
        #
        # for child in root.children:
        #     result += self.preorder(child)
        #
        # return result

        # iterative
        if not root:
            return []

        result, stack = [], [root]

        while stack:
            cur = stack.pop()
            result.append(cur.val)
            stack += reversed(cur.children)

        return result
