# Construct Quad Tree

"""
We want to use quad trees to store an N x N boolean grid. Each cell in the grid can only be true or false. The root node represents the whole grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same.

Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

Your task is to use a quad tree to represent a given grid. The following example may help you understand the problem better:

Note:

N is less than 1000 and guaranteened to be a power of 2.
If you want to know more about the quad tree, you can refer to its wiki.
"""

"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        N = len(grid)
        flattened = sum(grid, [])
        if len(set(flattened)) == 1:
            return Node(flattened[0], True, None, None, None, None)
        top_left = self.construct([l[0:N/2] for l in grid[0: N/2]])
        top_right = self.construct([l[N/2:N] for l in grid[0: N/2]])
        bottom_left = self.construct([l[0:N/2] for l in grid[N/2: N]])
        bottom_right = self.construct([l[N/2:N] for l in grid[N/2: N]])
        return Node('*', False, top_left, top_right, bottom_left, bottom_right)
