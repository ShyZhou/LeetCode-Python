# Leaf-Similar Trees

"""
Consider all the leaves of a binary tree. From left to right order, the values of those leaves form a leaf value sequence.

    3
   / \
  5   1
 /|  /\
6 2 9 8
 /|
7 4

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.leafSequence(root1) == self.leafSequence(root2)

    def leafSequence(self, root):
        if not root:
            return []
        res = []
        stk = [root]
        while stk:
            node = stk.pop()
            if not node.left and not node.right:
                res.append(node.val)
            if node.right:
                stk.append(node.right)
            if node.left:
                stk.append(node.left)
        return res
