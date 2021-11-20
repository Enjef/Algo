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

    def removeElements_v2(
            self,
            head: Optional[ListNode],
            val: int) -> Optional[ListNode]:  # 72.94% 90.11%
        if not head:
            return head
        while head and head.val == val:
            head = head.next
        dummy = ListNode(next=head)
        prev = dummy
        cur = head
        while head:
            while head and head.val == val:
                head = head.next
            prev.next = head
            if not head:
                break
            head = head.next
            prev = prev.next
        return dummy.next
