class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        # if not preorder:
        #     return
        #
        # root = TreeNode(preorder[0])
        # mid = inorder.index(root.val)
        #
        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        #
        # return root

        # better code

        def helper(stop):
            while inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())

                root.left = helper(root.val)
                inorder.pop()
                root.right = helper(stop)

                return root

        preorder.reverse()
        inorder.reverse()
        return helper(None)
