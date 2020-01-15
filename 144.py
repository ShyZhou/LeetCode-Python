# Binary Tree Preorder Traversal

# Given a binary tree, return the preorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        queue = [root]
        while queue:
            node = queue.pop()
            res.append(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return res
