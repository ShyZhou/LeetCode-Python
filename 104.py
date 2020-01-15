# Maximum Depth of Binary Tree

# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursion
class Solution():
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# iteration
import collections
class Solution():
    def maxDepth(self, root):
        if not root:
            return 0
        queue = collections.deque([root])
        res = 0
        while queue:
            res += 1
            num = len(queue)
            while num:
                node = queue.popleft()
                num -= 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
