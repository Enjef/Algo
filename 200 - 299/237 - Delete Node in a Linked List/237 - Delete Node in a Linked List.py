# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):  # 67.31% 62.98%
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    def deleteNode_mock(self, node):  # 96.43% 62.98%
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next and node.next.next:
            node.val = node.next.val
            node = node.next
        node.val = node.next.val
        node.next = None

    def deleteNode_best_speed(self, node):
        nextNode = node.next
        node.val = nextNode.val
        node.next = nextNode.next

    def deleteNode_best_memory(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
