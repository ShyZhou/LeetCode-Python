# Binary Tree Right Side View

"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        que = [root]
        next_level = [root]
        node_cnt = 1
        while node_cnt:
            res.append(next_level[-1].val)
            next_level = []
            for _ in range(node_cnt):
                node = que.pop(0)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            node_cnt = len(next_level)
            que += next_level
        return res
