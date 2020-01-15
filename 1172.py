# Dinner Plate Stacks

# You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum capacity.

# Implement the DinnerPlates class:

# DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks.
# void push(int val) pushes the given positive integer val into the leftmost stack with size less than capacity.
# int pop() returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all stacks are empty.
# int popAtStack(int index) returns the value at the top of the stack with the given index and removes it from that stack, and returns -1 if the stack with that given index is empty.

# Example:

# Input:
# ["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
# [[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
# Output:
# [null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]

# Explanation:
# DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
# D.push(1);
# D.push(2);
# D.push(3);
# D.push(4);
# D.push(5);         // The stacks are now:  2  4
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.popAtStack(0);   // Returns 2.  The stacks are now:     4
#                                                        1  3  5
#                                                        ﹈ ﹈ ﹈
# D.push(20);        // The stacks are now: 20  4
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.push(21);        // The stacks are now: 20  4 21
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
#                                                         1  3  5
#                                                         ﹈ ﹈ ﹈
# D.popAtStack(2);   // Returns 21.  The stacks are now:     4
#                                                         1  3  5
#                                                         ﹈ ﹈ ﹈
# D.pop()            // Returns 5.  The stacks are now:      4
#                                                         1  3
#                                                         ﹈ ﹈
# D.pop()            // Returns 4.  The stacks are now:   1  3
#                                                         ﹈ ﹈
# D.pop()            // Returns 3.  The stacks are now:   1
#                                                         ﹈
# D.pop()            // Returns 1.  There are no stacks.
# D.pop()            // Returns -1.  There are still no stacks.


# Constraints:

# 1 <= capacity <= 20000
# 1 <= val <= 20000
# 0 <= index <= 100000
# At most 200000 calls will be made to push, pop, and popAtStack.

# Time:  push: O(logn)
#        pop:  O(1), amortized
#        popAtStack: O(logn)
# Space: O(n * c)

import heapq
class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.__stks = []
        self.__c = capacity
        self.__min_heap = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.__min_heap:
            l = heapq.heappop(self.__min_heap)
            if l < len(self.__stks):
                self.__stks[l].append(val)
                return
            self.__min_heap = []  # nothing is valid in min heap
        if not self.__stks or len(self.__stks[-1]) == self.__c:
            self.__stks.append([])
        self.__stks[-1].append(val)

    def pop(self):
        """
        :rtype: int
        """
        while self.__stks and not self.__stks[-1]:
            self.__stks.pop()
        if not self.__stks:
            return -1
        return self.__stks[-1].pop()

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index >= len(self.__stks) or not self.__stks[index]:
            return -1
        heapq.heappush(self.__min_heap, index)
        return self.__stks[index].pop()



# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
