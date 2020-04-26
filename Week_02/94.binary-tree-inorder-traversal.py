class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # recursive

        # if not root:
        #     return []
        #
        # result = []
        #
        # result += self.inorderTraversal(root.left)
        # result.append(root.val)
        # result += self.inorderTraversal(root.right)
        #
        # return result

        # iterative

        result, stack = [], []

        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right

        return result
