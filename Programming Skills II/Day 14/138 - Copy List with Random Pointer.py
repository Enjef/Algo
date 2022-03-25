"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head):  # 14.81% 52.56%
        if not head:
            return head
        nodes = {}
        cur = head
        while cur:
            nodes[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                nodes[cur].next = nodes[cur.next]
            if cur.random:
                nodes[cur].random = nodes[cur.random]
            cur = cur.next
        return nodes[head]

    def copyRandomList_best_speed(self, head: 'Node') -> 'Node':
        if not head:
            return None
        p = head
        while p:
            copy = Node(p.val)
            copy.next = p.next
            p.next = copy
            p = copy.next
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        p = head
        newHead = head.next
        while p:
            temp = p.next
            p.next = temp.next
            if temp.next:
                temp.next = temp.next.next
            p = p.next
        return newHead

    def copyRandomList_3nd_best_speed(self, head):
        root = prev =  Node(0)
        dic = {}
        cur = head 
        while cur:
            t_new = Node(cur.val)
            dic[cur] = t_new
            prev.next = t_new
            prev = prev.next
            cur = cur.next
        cur = head
        while cur:
            if cur.random:
                dic[cur].random = dic[cur.random]
            cur = cur.next
        return root.next

    def copyRandomList_best_memory(self, head):
        hashTree = {None:None}
        temp = head
        while temp:
            hashTree[temp]=Node(temp.val)
            temp = temp.next
        temp = head
        while temp:
            copy = hashTree[temp]
            copy.next = hashTree[temp.next]
            copy.random = hashTree[temp.random]
            temp = temp.next
        return hashTree[head]
