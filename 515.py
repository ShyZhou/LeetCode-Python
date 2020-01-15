# Find Largest Value in Each Tree Row

# You need to find the largest value in each row of a binary tree.

# Example:
# Input:

#           1
#          / \
#         3   2
#        / \   \
#       5   3   9

# Output: [1, 3, 9]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, level = [], root and [root]
        while level:
            res.append(max(n.val for n in level))
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return res
