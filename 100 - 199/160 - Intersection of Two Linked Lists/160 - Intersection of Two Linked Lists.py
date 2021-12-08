# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(
            self,
            headA: ListNode,
            headB: ListNode) -> Optional[ListNode]:  # 9.13% 5.60%
        seen = set()
        while headA or headB:
            if headA:
                if headA in seen:
                    return headA
                seen.add(headA)
                headA = headA.next
            if headB:
                if headB in seen:
                    return headB
                seen.add(headB)
                headB = headB.next
        return None

    def getIntersectionNode_best_speed(
            self,
            headA: ListNode,
            headB: ListNode) -> ListNode:
        l1 = l2 = 0
        node = headA
        while node:
            l1 += 1
            node = node.next
        node = headB
        while node:
            l2 += 1
            node = node.next
        nodeA, nodeB = headA, headB
        while l1 > l2:
            l1 -= 1
            nodeA = nodeA.next
        while l2 > l1:
            l2 -= 1
            nodeB = nodeB.next
        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
        return None

    def getIntersectionNode_2nd_to_best_speed(
            self,
            headA: ListNode,
            headB: ListNode) -> ListNode:
        d = set()
        while headA is not None:
            d.add(headA)
            headA=headA.next
        while headB is not None:
            if headB in d:
                return headB
            headB=headB.next
        return None

    def getIntersectionNode_best_memory(self, headA, headB):
        p, q = headA, headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p
