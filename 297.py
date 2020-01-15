# Serialize and Deserialize Binary Tree

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Example:

# You may serialize the following tree:

#     1
#    / \
#   2   3
#      / \
#     4   5

# as "[1,2,3,null,null,4,5]"

# Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 二叉树的先序遍历
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def traverse(node):
            if node:
                vals.append(str(node.val))
                traverse(node.left)
                traverse(node.right)
            else:
                vals.append('#')

        vals = []
        traverse(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def construct():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = construct()
            node.right = construct()
            return node

        vals = iter(data.split())
        return construct()

# 二叉树的层次遍历
class Codec:
    def serialize(self, root):
        if not root:
            return []
        res = [root.val]
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            res.append(node.left.val if node.left else 'null')
            res.append(node.right.val if node.right else 'null')
        while res and res[-1] == null:
            res.pop()
        return '[' + ','.join(map(str, res)) + ']'

    def deserialize(self, data):
        if data == '[]':
            return None
        nodes = collections.deque([[TreeNode(i), None][i == 'null'] for i in data[1:-1].split(',')])
        q = collections.deque([nodes.popleft()]) if nodes else None
        root = q[0] if q else None
        while q:
            parent = q.popleft()
            left = nodes.popleft() if nodes else None
            right = nodes.popleft() if nodes else None
            parent.left, parent.right = left, right
            if left:
                q.append(left)
            if right:
                q.append(right)
        return root

# json + tuple
class Codec:
    def serialize(self, root):
        def tuplify(root):
            return root and (root.val, tuplify(root.left), tuplify(root.right))
        return json.dumps(tuplify(root))

    def deserialize(self, data):
        def detuplify(t):
            if t:
                root = TreeNode(t[0])
                root.left = detuplify(t[1])
                root.right = detuplify(t[2])
                return root
        return detuplify(json.loads(data))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))