# Minimum Depth of Binary Tree

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursion
class Solution():
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        else:
            return 1 + self.minDepth(root.left) + self.minDepth(root.right)

# iteration
import collections
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = collections.deque([root])
        res = 0
        while queue:
            res += 1
            num = len(queue)
            while num:
                node = queue.popleft()
                if not node.left and not node.right:
                    return res
                num -= 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
