# Maximum Depth of N-ary Tree

"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:

    1
  / | \
 3  2  4
/ \
5  6

We should return its max depth, which is 3.

Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if root.children is None:
            return 1
        depth = 0
        for child in root.children:
            depth = max(self.maxDepth(child), depth)
        return depth + 1

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        res = 0
        que = collections.deque()
        que.append(root)
        while que:
            new_level = False
            for _ in range(len(que)):
                node = que.popleft()
                if not node:
                    continue
                new_level = True
                for child in node.children:
                    que.append(child)
            if new_level:
                res += 1
        return res
