# Linked List Cycle

# Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# 3 -> 2 -> 0 -> -4
#      ^          |
#      |          |
#      - - - - - -

# Example 2:

# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.

# 1 -> 2
# ^    |
# |    |
#  - - -

# Example 3:

# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# 1

# Follow up:

# Can you solve it using O(1) (i.e. constant) memory?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                return True
        return False

# II

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Note: Do not modify the linked list.

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# 3 -> 2 -> 0 -> -4
#      ^          |
#      |          |
#      - - - - - -

# Example 2:

# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.

# 1 -> 2
# ^    |
# |    |
#  - - -

# Example 3:

# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.

# 1

# Follow-up:
# Can you solve it without using extra space?

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                break
        if fast is None or fast.next is None:
            return None
        slow = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow
