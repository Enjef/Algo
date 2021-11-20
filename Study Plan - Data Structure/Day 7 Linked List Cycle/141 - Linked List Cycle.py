class Solution:
    def hasCycle(self, head: ListNode) -> bool:  # 6.64%
        if not head:
            return False
        unique = set()
        while head:
            if head in unique:
                return True
            else:
                unique.add(head)
                head = head.next
        return False

    def hasCycle_2(self, head: Optional[ListNode]) -> bool:  # 82.91% 17.82%
        check = set()
        while head:
            if head in check:
                return True
            check.add(head)
            head = head.next
        return False

    def hasCycle_v3(self, head: ListNode) -> bool:  # 99.77% 25.71%
        if not head:
            return False
        slow = head
        fast = head.next
        while fast:
            if slow == fast:
                return True
            if fast.next is None:
                break
            slow = slow.next
            fast = fast.next.next
        return False
