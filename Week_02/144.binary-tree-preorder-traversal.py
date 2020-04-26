class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # recursive

        # if not root:
        #     return []
        #
        # result = [root.val]
        #
        # result += self.preorderTraversal(root.left)
        # result += self.preorderTraversal(root.right)
        #
        #
        # return result

        # iterative

        result, stack = [], [root]

        while stack:
            cur = stack.pop()

            if cur:
                result.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)

        return result
