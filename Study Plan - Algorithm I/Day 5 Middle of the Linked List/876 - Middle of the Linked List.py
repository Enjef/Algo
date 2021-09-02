class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast.next:
            fast = fast.next.next
            slow = slow.next
            if not fast:
                break
        return slow
