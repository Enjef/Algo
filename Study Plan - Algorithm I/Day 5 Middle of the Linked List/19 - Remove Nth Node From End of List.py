class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next
            n -= 1
            if n < 0:
                slow = slow.next
        if slow == head and n == 1:
            return head.next
        slow.next = slow.next.next
        return head
