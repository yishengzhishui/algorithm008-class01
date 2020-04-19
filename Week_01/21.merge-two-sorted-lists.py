class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # recursive
        # while l1 and l2:
        #     if l1.val > l2.val:
        #         l1, l2 = l2, l1
        #         l1.next = self.mergeTwoLists(l1.next, l2)
        #
        # return l1 or l2

        # iterative
        dummy = ListNode(0)
        pre = dummy

        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next

        pre.next = l1 or l2

        return dummy.next


