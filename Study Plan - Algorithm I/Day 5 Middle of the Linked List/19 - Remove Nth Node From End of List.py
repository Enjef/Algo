class Solution:
    def removeNthFromEnd(
            self,
            head: ListNode,
            n: int) -> ListNode:  # 32.46% 46.81%
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

    def removeNthFromEnd_second_atempt(
            self,
            head: Optional[ListNode],
            n: int) -> Optional[ListNode]:  # 81.77% 14.29%
        if not head.next:
            return head.next
        dummy = ListNode(next=head)
        first = second = head
        while second.next:
            second = second.next
            if n <= 0:
                first = first.next
            n -= 1
        if n > 0:
            return first.next
        first.next = first.next.next
        return dummy.next
