# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(
            self,
            head: Optional[ListNode]) -> Optional[ListNode]:  # 25.86% 9.96%
        seen = set()
        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
        return None

    def detectCycle_best_speed(self, head: ListNode) -> ListNode:
        node_dict = {}
        cur = head
        pos = 0
        while cur:
            node_dict[cur] = pos
            cur = cur.next
            if cur in node_dict:
                return cur
        return None

    def detectCycle_best_memory(self, head: ListNode) -> ListNode:
        x = head
        while x :
            if x.val == "xx":
                return x
            if x == None:
                return -1
            x.val = "xx"
            x = x.next
