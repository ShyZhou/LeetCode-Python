# Reverse Linked List

"""
Reverse a singly linked list.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        p = head
        head = None
        while p is not None:
            after = p.next
            p.next = head
            head = p
            p = after

        return head