# Longest Univalue Path

"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

Example 1:
Input:
    5
   / \
  4   5
 / \   \
1   1   5
Output: 2

Example 2:
Input:
    1
   / \
  4   5
 / \   \
4   4   5
Output: 2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ans = 0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longestPath(root)
        return self.ans

    def longestPath(self, node):
        if not node:
            return 0
        left_length = self.longestPath(node.left)
        right_length = self.longestPath(node.right)
        left_arrow = right_arrow = 0
        if node.left and node.left.val == node.val:
            left_arrow = left_length + 1
        if node.right and node.right.val == node.val:
            right_arrow = right_length + 1
        self.ans = max(self.ans, left_arrow + right_arrow)
        return max(left_arrow, right_arrow)
