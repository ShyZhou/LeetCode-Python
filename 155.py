# Min Stack

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.min_stk = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.min_stk) == 0 or x <= self.min_stk[-1]:
            self.min_stk.append(x)
        self.stk.append(x)


    def pop(self):
        """
        :rtype: void
        """
        if len(self.stk) == 0:
            return
        if self.stk[-1] == self.min_stk[-1]:
            del self.min_stk[-1]
        del self.stk[-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()