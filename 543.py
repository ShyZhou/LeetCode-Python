# Diameter of Binary Tree

"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Diameter is the sum of the height of the left and right subtree
class Solution(object):
    height = {}
    def getHeight(self, root):
        if not root:
            return 0
        if root in self.height:
            return self.height[root]
        self.height[root] = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        return self.height[root]

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.getHeight(root.left) + self.getHeight(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
