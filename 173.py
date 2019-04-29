# Binary Search Tree Iterator

"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Example:
  7
 / \
3  15
   / \
  9  20

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false


Note:
next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Python generators: https://realpython.com/introduction-to-python-generators/
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.last = root
        while self.last and self.last.right:
            self.last = self.last.right
        self.current = None
        self.g = self.iterator(root)


    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return next(self.g)


    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.current is not self.last


    def iterator(self, node):
        if not node:
            return
        for x in self.iterator(node.left):
            yield x
        self.current = node
        yield node.val
        for x in self.iterator(node.right):
            yield x


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()