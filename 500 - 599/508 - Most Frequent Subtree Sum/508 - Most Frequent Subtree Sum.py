# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(
            self, root: Optional[TreeNode]) -> List[int]:  # 5.01% 75.42%
        def dfs(node):
            if not node:
                return 0
            cur = node.val + dfs(node.left) + dfs(node.right)
            counter[cur] += 1
            return cur
        
        counter = defaultdict(int)
        dfs(root)        
        return [x for x in counter if counter[x] == max(counter.values())]

    def findFrequentTreeSum_best_speed(
            self, root: Optional[TreeNode]) -> List[int]:
        self.counter = defaultdict(int)
        self.max_freq = [0, []]

        def dfs(root):
            if not root:
                return 0
            left_s, right_s = dfs(root.left), dfs(root.right)
            _sum = left_s+right_s+root.val
            self.counter[_sum]+=1
            if self.counter[_sum]>self.max_freq[0]:
                self.max_freq[0] = self.counter[_sum]
                self.max_freq[1] = []
            if self.counter[_sum]==self.max_freq[0]:
                self.max_freq[1].append(_sum)
            return _sum
        dfs(root)
        return self.max_freq[1]

    def findFrequentTreeSum_best_memory(
            self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)
        roots = [[0, -1]]
        children = [(None, 0), (root, 0)]
        while children:
            node, rank = children.pop()
            while roots[-1][1] >= rank:
                value = roots.pop()[0]
                count[value] += 1
                roots[-1][0] += value
            if node is None:
                continue
            if node.left or node.right:
                roots.append([node.val, rank])
                if node.left:
                    children.append((node.left, rank+1)) 
                if node.right:
                    children.append((node.right, rank+1))
            else:
                count[node.val] += 1
                roots[-1][0] += node.val
        mx = max(count.values())
        return [k for k in count if count[k] == mx]
