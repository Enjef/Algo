# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:  # 18.14% 42.90%

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        out = []
        if not root:
            return ''
        stack = [root]
        while stack:
            temp = []
            while stack:
                cur = stack.pop(0)
                if not cur:
                    out.append(None)
                    continue
                out.append(cur.val)
                temp.extend([cur.left, cur.right])
            stack = temp
        while out[-1] is None:
            out.pop()
        return ','.join(
            [str(x) if isinstance(x, int) else 'null' for x in out])
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        level = 2
        index = 1
        j = 0
        root = TreeNode(val=data[0])
        parent = [root]
        while index < len(data):
            child = [TreeNode(val=x) for x in data[index:index+level]]
            index = index + level
            level *= 2 
            for i in range(0, len(child), 2):
                parent[j].left = child[i] if i < len(child) else None
                parent[j].right = child[i+1] if i+1 < len(child) else None
                j += 1
            parent.extend(child)
        return root



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

class Codec_best_speed:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        res = [root.val]
        q = collections.deque([root])
        while q:
            front = q.popleft()
            res.append('null')
            if front.left:
                q.append(front.left)
                res[-1] = front.left.val
            res.append('null')
            if front.right:
                q.append(front.right)
                res[-1] = front.right.val
        while res and res[-1] == 'null':
            res.pop()
  
        return ','.join(map(str,res))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        print(data)
        vals = data.split()
        print(vals[0])
        root = TreeNode(vals[0])
        return root

class Codec_memory_with_build_tree:

    def serialize(self, root):
        if root == None:
            return 'X,'
        leftserilized = self.serialize(root.left)
        rightserilized = self.serialize(root.right)
        return str(root.val) + ',' + leftserilized + rightserilized

    def deserialize(self, data):
        data = data.split(',')
        root = self.buildTree(data)
        return root 
    
    def buildTree(self,data):
        val = data.pop(0)
        if val == 'X':
            return None
        node = TreeNode(val)
        node.left = self.buildTree(data)
        node.right = self.buildTree(data)
        return node
