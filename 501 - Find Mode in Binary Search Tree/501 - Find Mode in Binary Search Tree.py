# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:  # 68.09% 44.01%
        out = []
        x_dict = self.helper(root, {})
        x_key = list(x_dict.keys())
        x_val = list(x_dict.values())
        x_max = max(x_val)
        for i in range(len(x_val)):
            if x_val[i] == x_max:
                out.append(x_key[i])
        return out

    def helper(self, root, x_dict):
        if root.val not in x_dict:
            x_dict[root.val] = 0
        x_dict[root.val] += 1
        if root.left:
            self.helper(root.left, x_dict)
        if root.right:
            self.helper(root.right, x_dict)
        return x_dict

    def findMode_s_to_best(self, root: TreeNode) -> List[int]:  # 40 ms
        tmp = defaultdict(int)
        def recurse(node):
            if not node:
                return
            tmp[node.val] += 1
            recurse(node.left)
            recurse(node.right)
        recurse(root)
        max_freq = max(tmp.values())
        return [key for key in tmp if tmp[key] == max_freq]

    def findMode_best(self, root: TreeNode) -> List[int]:  # 36 ms
        d = {}
        res = []
        currmax = 0
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node.val in d:
                d[node.val] = 0
            d[node.val] += 1
            if d[node.val] > currmax:
                currmax = d[node.val]
                res.clear()
                res.append(node.val)
            elif d[node.val] == currmax:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res

    def findMode_memory_best(self, root: TreeNode) -> List[int]:
        nowNode = None
        nodeStack = [root]
        outList = []
        nowVal = 0
        count = 0
        Max = 0
        while len(nodeStack) > 0:
            nowNode = nodeStack.pop()
            if nowNode.left == None and nowNode.right == None:
                if count == 0:
                    nowVal = nowNode.val
                    count = 1
                else:
                    if nowNode.val == nowVal:
                        count += 1
                    else:
                        if count > Max:
                            outList = [nowVal]
                            Max = count
                        elif count == Max:
                            outList.append(nowVal)
                        nowVal = nowNode.val
                        count = 1
                continue
            if nowNode.right != None:
                nodeStack.append(nowNode.right)
                nowNode.right = None
            nodeStack.append(nowNode)
            if nowNode.left != None:
                nodeStack.append(nowNode.left)
                nowNode.left = None
        if count > Max:
            outList = [nowVal]
        elif count == Max:
            outList.append(nowVal)
        return outList
