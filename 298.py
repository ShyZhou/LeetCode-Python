# Binary Tree Longest Consecutive Sequence

# Given a Binary Tree find the length of the longest path which comprises of nodes with consecutive values in increasing order. Every node is considered as a path of length 1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, cur_length, expected_val, res):
        if not root:
            return

        if root.val == expected_val:
            cur_length += 1
        else:
            cur_length = 1

        res = max(res, cur_length)

        self.helper(root.left, cur_length, root.val + 1, res)
        self.helper(root.right, cur_length, root.val + 1, res)

    def LCS(self, root):
        res = 0
        self.helper(root, 0, root.val, res)
        return res
