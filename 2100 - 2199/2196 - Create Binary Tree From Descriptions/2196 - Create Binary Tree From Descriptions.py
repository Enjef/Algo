# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 86.44% 32.92%
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        roots = dict()
        children = set()
        for parent, child, isLeft in descriptions:
            children.add(child)
            if child not in roots:
                roots[child] = TreeNode(val=child)
            if parent not in roots:
                roots[parent] = TreeNode(val=parent)
            if not isLeft:
                roots[parent].right = roots[child]
            if isLeft:
                roots[parent].left = roots[child]
        return roots[(set(roots)-children).pop()]

    def createBinaryTree_best_speed(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodeMap = dict()
        parents = set()
        children = set()
        for description in descriptions:
            parent, child, isLeft = description
            parents.add(parent)
            children.add(child)
            parentNode = nodeMap.get(parent)
            if parentNode is None:
                parentNode = TreeNode(parent)
                nodeMap[parent] = parentNode
            childNode = nodeMap.get(child)
            if childNode is None:
                childNode = TreeNode(child)
                nodeMap[child] = childNode
            if isLeft:
                parentNode.left = childNode
            else:
                parentNode.right = childNode

        for p in parents:
            if p not in children:
                root = nodeMap.get(p)
                break
        return root

    def createBinaryTree_best_memory(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        root = None
        for i in range(len(descriptions)):
            children.add(descriptions[i][1])
            nodes[descriptions[i][0]] = TreeNode(
                descriptions[i][0], None, None)
            nodes[descriptions[i][1]] = TreeNode(
                descriptions[i][1], None, None)
        for i in range(len(descriptions)):
            if descriptions[i][0] not in children:
                root = descriptions[i][0]
            if descriptions[i][2] == 1:
                nodes[descriptions[i][0]].left = nodes[descriptions[i][1]]
            else:
                nodes[descriptions[i][0]].right = nodes[descriptions[i][1]]
        return nodes[root]
