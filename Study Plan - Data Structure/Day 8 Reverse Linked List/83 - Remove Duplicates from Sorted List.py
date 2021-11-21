class Solution:
    def deleteDuplicates(
            self,
            head: Optional[ListNode]) -> Optional[ListNode]:  # # 5.51% 55.88%
        if not head:
            return head
        cur = head
        while cur:
            if cur.next:
                if cur.next.val == cur.val:
                    cur.next = cur.next.next
                    continue
            cur = cur.next
        return head

    def deleteDuplicates_v2(
            self,
            head: Optional[ListNode]) -> Optional[ListNode]:  # 59.65% 58.51%
        dummy = prev = ListNode(next=head)
        while head and head.next:
            while head and head.next and head.val == head.next.val:
                    head = head.next
            prev.next = head
            prev = head
            head = head.next
        return dummy.next
