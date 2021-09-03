class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        while head.val == val:
            if not head.next:
                return None
            head = head.next
        prev = ListNode(next=head)
        cur = head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return head
