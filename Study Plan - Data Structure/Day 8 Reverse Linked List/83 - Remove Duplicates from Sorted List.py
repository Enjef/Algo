class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
