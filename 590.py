# N-ary Tree Postorder Traversal

"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:
    1
  / | \
 3  2  4
/ \
5  6

Return its postorder traversal as: [5,6,3,2,4,1].

Note:
Recursive solution is trivial, could you do it iteratively?
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        for child in root.children:
            res += self.postorder(child)
        return res + [root.val]
