# N-ary Tree Preorder Traversal

"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:
    1
  / | \
 3  2  4
/ \
5  6

Return its preorder traversal as: [1,3,5,6,2,4].

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
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        res = [root.val]
        for child in root.children:
            res += self.preorder(child)
        return res

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            children = []
            for child in node.children:
                children.insert(0, child)
            stack += children
        return res
