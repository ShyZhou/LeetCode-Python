# Minimum Absolute Difference in BST

"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

Note: There are at least two nodes in this BST.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find_max(self, node):
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node

    def find_min(self, node):
        current_node = node
        while current_node.left:
            current_node = current_node.left
        return current_node

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        minum = float('inf')
        if not root:
            return minum
        if root.left:
            minum = min(minum, (root.val - self.find_max(root.left).val))
        if root.right:
            minum = min(minum, (self.find_min(root.right).val - root.val))
        return min(minum, self.getMinimumDifference(root.left), self.getMinimumDifference(root.right))
