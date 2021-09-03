class Solution:
    def hasCycle(self, head: ListNode) -> bool:
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
