# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 7.31%  93.81%
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            new = head.next
            head.next = prev
            prev = head
            head = new
        return prev

    # 84.59% 9.06%
    def reverseList_v2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(prev, cur):
            if cur is None:
                return
            next_ = cur.next
            self.new = cur
            cur.next = prev
            helper(cur, next_)

        self.new = None
        helper(None, head)
        return self.new
