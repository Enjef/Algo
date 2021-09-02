# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):  # 51.25% 15.76%
        current = head
        x_prev = None
        x_node = head
        if not head.next:
            return None
        while n:
            n -= 1
            current = current.next
        while current:
            current = current.next
            x_prev = x_node
            x_node = x_node.next
        if x_prev is None:
            return head.next
        x_prev.next = x_node.next
        return head

    def removeNthFromEnd_study_plan_day_5(
            self,
            head: ListNode,
            n: int) -> ListNode:  # 17.93% 48.49%
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

    def removeNthFromEnd_best_speed(
            self,
            head: Optional[ListNode],
            n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        m = 1
        node = head
        while node.next:
            m += 1
            node = node.next
        if n != m:
            node = head
            while m > n+1:
                m -= 1
                node = node.next
            if node.next:
                node.next = node.next.next
        else:
            return head.next
        return head

    def removeNthFromEnd_sec_to_best_memory(
            self,
            head: Optional[ListNode],
            n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n+1):
            second = second.next
        while second:
            first = first.next
            second = second.next
        first.next = first.next.next
        return dummy.next
