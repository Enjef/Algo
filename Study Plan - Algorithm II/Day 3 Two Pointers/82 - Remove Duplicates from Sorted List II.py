class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode()
        dummy.next = head
        while head:
            if head.next and head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                prev.next = head
            else:
                prev = head
                head = head.next
        return dummy.next
