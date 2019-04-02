# Convert BST to Greater Tree

"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
      5
    /   \
   2     13

Output: The root of a Greater Tree like this:
     18
    /   \
  20     13
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    inorder = []
    greaterval = {}
    def inordertraverse(self, root):
        if not root:
            return []
        return self.inordertraverse(root.left) + [root.val] + self.inordertraverse(root.right)

    def calgreaterval(self, vals):
        for i, v in enumerate(vals):
            self.greaterval[v] = sum(vals[i : len(vals)])

    def assignval(self, root):
        if not root:
            return None
        root.val = self.greaterval[root.val]
        root.left = self.assignval(root.left)
        root.right = self.assignval(root.right)
        return root

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.inorder = self.inordertraverse(root)
        self.calgreaterval(self.inorder)
        return self.assignval(root)
