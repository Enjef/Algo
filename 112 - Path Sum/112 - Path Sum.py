# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curr_a, curr_b = headA, headB
        while curr_a != curr_b:
            curr_a = curr_a.next if curr_a else headB
            curr_b = curr_b.next if curr_b else headA
        return curr_a

    def getIntersection_set(self, headA: ListNode, headB: ListNode) -> ListNode:
        set_a = set()
        while headA:
            set_a.add(headA)
            headA = headA.next
        while headB:
            if headB in set_a:
                return headB
            headB = headB.next
        return None
